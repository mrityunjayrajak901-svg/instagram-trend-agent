import requests
TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"
OPENROUTER_API_KEY = "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"

prompt = """
Give today's viral Instagram AI editing trend.

Include:

1. Trend Name
2. Viral Score
3. Cinematic Prompt
4. Caption
5. Hashtags
   """

response = requests.post(
"https://openrouter.ai/api/v1/chat/completions",
headers={
"Authorization": f"Bearer {OPENROUTER_API_KEY}",
"Content-Type": "application/json"
},
json={
"model": "deepseek/deepseek-chat",
"messages": [
{
"role": "user",
"content": prompt
}
]
}
)

data = response.json()

message = data["choices"][0]["message"]["content"]

telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
telegram_url,
data={
"chat_id": CHAT_ID,
"text": message
}
)

print("Message sent successfully")
