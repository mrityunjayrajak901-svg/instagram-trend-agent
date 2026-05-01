import requests

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"

prompt = """
Give today's viral Instagram AI photo editing trend.
Include:

1. Trend name
2. Viral score (1-100)
3. Cinematic AI editing prompt (very detailed)
4. Caption
5. Hashtags
   """

try:
response = requests.post(
"https://openrouter.ai/api/v1/chat/completions",
headers={
"Authorization": f"Bearer {OPENROUTER_API_KEY}",
"Content-Type": "application/json"
},
json={
"model": "openai/gpt-3.5-turbo",
"messages": [{"role": "user", "content": prompt}]
},
timeout=20
)

data = response.json()

if "choices" in data:
    message = data["choices"][0]["message"]["content"]
else:
    message = str(data)

except Exception as e:
message = f"Bot Error: {str(e)}"

telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
telegram_url,
data={
"chat_id": CHAT_ID,
"text": message[:3500]
}
)

print("DONE")
