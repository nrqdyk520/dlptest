import subprocess
#这是一个test

# 主机列表
hosts = [
    "ai-model.idc.sse",
    "appsmith.idc.sse",
    "argocd.idc.sse",
    "console-fass.idc.sse",
    "console-mass.idc.sse",
    "console-minio.idc.sse",
    "console-minio-main-storage.idc.sse",
    "daguan.idc.sse",
    "dockerhub.idc.sse",
    "docker.idc.sse",
    "fass.idc.sse",
    "gocd.idc.sse",
    "grafana.idc.sse",
    "k8s-demo.idc.sse",
    "kafka-ui.idc.sse",
    "kibana.idc.sse",
    "longhorn.idc.sse",
    "minio-main-storage.idc.sse",
    "nexus.idc.sse",
    "nexus-registry.idc.sse",
    "nginx.idc.sse",
    "ollama.idc.sse",
    "open-webui.idc.sse",
    "pgadmin.idc.sse",
    "pgo.idc.sse",
    "prometheus.idc.sse",
    "registry.idc.sse",
    "superset2.idc.sse",
    "superset.idc.sse",
    "test-ai-model.idc.sse",
    "test-k8s-demo.idc.sse",
    "kafka.idc.sse",
    "minio.idc.sse",
    "logstash.idc.sse",
    "efk3s.idc.sse",
    "k3s.idc.sse",
    "vip.idc.sse",
    "postgresql.idc.sse",
    "pg14.idc.sse",
    "pg16.idc.sse",
    "mass.idc.sse"
]

def ping_host(host):
    try:
        result = subprocess.run(["ping", "-n", "1", host], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def main():
    unreachable_hosts = []
    for host in hosts:
        print(f"Pinging {host}...")
        if not ping_host(host):
            unreachable_hosts.append(host)
            print(f"{host} is not reachable.")
        print("-" * 40)

    try:
        with open("ping_results.txt", "w", encoding='utf-8') as f:
            if unreachable_hosts:
                f.write("\n".join(unreachable_hosts))
        print("Results written to ping_results.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
