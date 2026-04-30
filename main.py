import requests


YOUR CREDENTIALS


TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"
OPENROUTER_API_KEY = "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"


AI PROMPT


prompt = """
You are an Instagram AI Trend Prediction Agent.

Give:

1. Today's viral Instagram AI editing trend
2. Viral Score
3. Cinematic AI photo editing prompt
4. Caption
5. Hashtags

Focus on:

- Luxury cinematic portraits
- Neon rain aesthetics
- Dark moody edits
- Viral Instagram explore styles
- Emotional storytelling visuals
  """


OPENROUTER API REQUEST


response = requests.post(
"https://openrouter.ai/api/v1/chat/completions",
headers={
"Authorization": f"Bearer {OPENROUTER_API_KEY}",
"Content-Type": "application/json"
},
json={
"model": "openai/gpt-3.5-turbo",
"messages": [
{
"role": "user",
"content": prompt
}
]
}
)


RESPONSE HANDLE


data = response.json()

print(data)

if "choices" in data:
message = data["choices"][0]["message"]["content"]
else:
message = f"API Error:\n{data}"


SEND TO TELEGRAM


telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
telegram_url,
data={
"chat_id": CHAT_ID,
"text": message
}
)

print("Message sent successfully")
