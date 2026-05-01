import requests

TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"
OPENROUTER_API_KEY = "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"

prompt = """
Give today's viral Instagram AI editing trend with:

1. Trend name
2. Viral score
3. Editing prompt
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

print("Done")
