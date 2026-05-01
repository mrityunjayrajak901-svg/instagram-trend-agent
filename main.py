import requests

TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"
OPENROUTER_API_KEY = "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"

prompt = "Give one viral Instagram AI photo editing trend with cinematic prompt, caption and hashtags."

response = requests.post(
url="https://openrouter.ai/api/v1/chat/completions",
headers={
"Authorization": f"Bearer {OPENROUTER_API_KEY}",
"Content-Type": "application/json",
"HTTP-Referer": "https://openrouter.ai",
"X-Title": "Instagram Trend Agent"
},
json={
"model": "mistralai/mistral-7b-instruct:free",
"messages": [
{
"role": "user",
"content": prompt
}
]
}
)

data = response.json()

if "choices" in data:
   message = data["choices"][0]["message"]["content"]
else:
   message = str(data)

requests.post(
f"https://api.telegram.org/bot{TOKEN}/sendMessage",
data={
"chat_id": CHAT_ID,
"text": message
}
)

print("Done")
