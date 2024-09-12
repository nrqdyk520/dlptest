import win32com.client as win32
from datetime import datetime, timedelta, timezone

def read_emails(folder_name="收件箱", subfolders=None):
    if subfolders is None:
        subfolders = ["王晨", "奕佳婷", "张金凤"]

    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.Folders.Item("sp.chris.dai@enflame-tech.com").Folders.Item(folder_name)
    
    results = []
    five_days_ago = datetime.now(timezone.utc) - timedelta(days=5)
    
    for subfolder_name in subfolders:
        try:
            folder = inbox.Folders.Item(subfolder_name)
            messages = folder.Items
            messages.Sort("[ReceivedTime]", True)
        
            for msg in messages:
                try:
                    sender_name = msg.SenderName if msg.SenderName else "<unknown>"
                    received_time = msg.ReceivedTime
                    # Ensure received_time is aware datetime
                    received_time = received_time.replace(tzinfo=timezone.utc)

                    print(f"Processing message from: {sender_name} in folder: {subfolder_name}")
                    print(f"Received time: {received_time}")

                    if received_time >= five_days_ago:
                        subject = msg.Subject
                        from_ = sender_name
                        body = msg.Body
                        results.append((subject, from_, body))
                    else:
                        print("Message is older than five days, skipping.")
                except Exception as e:
                    print(f"Error reading message: {e}")
        except Exception as e:
            print(f"Error accessing folder {subfolder_name}: {e}")
    
    return results

if __name__ == "__main__":
    emails = read_emails()
    for subject, from_, body in emails:
        print(f"Subject: {subject}\nFrom: {from_}\n\n{body}\n{'-'*80}\n")
