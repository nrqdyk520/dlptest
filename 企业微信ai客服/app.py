from flask import Flask, request, jsonify
from dashscope import Application
from http import HTTPStatus
import time

app = Flask(__name__)

# 通义千问API配置
TONGYIQIANWEN_API_KEY = 'sk-bcfda4d6de634385b661f7a59d3a6697'
APP_ID = 'fde4eb8b664c4100af06037e3d18e864'

def call_agent_app(prompt):
    response = Application.call(
        app_id=APP_ID,
        prompt=prompt,
        api_key=TONGYIQIANWEN_API_KEY,
    )

    if response.status_code != HTTPStatus.OK:
        return None, 'request_id=%s, code=%s, message=%s' % (response.request_id, response.status_code, response.message)
    else:
        return response.output, None

@app.route('/wechat', methods=['POST'])
def wechat():
    data = request.json
    user_message = data['Content']

    # 调用通义千问API获取回复
    model_reply, error = call_agent_app(user_message)

    if error:
        model_reply = f"Error: {error}"

    # 构建企业微信的回复消息
    reply_message = {
        "ToUserName": data['FromUserName'],
        "FromUserName": data['ToUserName'],
        "CreateTime": int(time.time()),
        "MsgType": "text",
        "Content": model_reply
    }

    return jsonify(reply_message)

if __name__ == '__main__':
    app.run(port=5000)
