import requests

services = {
    "OpenAI": "https://api.openai.com",
    "Google": "https://www.google.com",
    "GitHub": "https://www.github.com"
}

def check_services():
    status = {}
    for name, url in services.items():
        try:
            r = requests.get(url, timeout=2)
            status[name] = r.status_code
        except:
            status[name] = "DOWN"
    return status
