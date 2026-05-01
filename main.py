from http.server import BaseHTTPRequestHandler, HTTPServer

def run_bot():
    import requests

    TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
    CHAT_ID = "7008909688"
    OPENROUTER_API_KEY = "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"

    prompt = "Give today's viral Instagram AI trend"

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    data = response.json()

    message = data.get("choices", [{}])[0].get("message", {}).get("content", str(data))

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message}
    )

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        run_bot()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

port = 10000
server = HTTPServer(("0.0.0.0", port), handler)
server.serve_forever()
