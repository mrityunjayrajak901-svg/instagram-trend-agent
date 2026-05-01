import requests

TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"
OPENROUTER_API_KEY = "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"

prompt = """
You are an expert Instagram AI Trend Analyst.

Your task is to predict the most viral AI photo editing trend for today.

Give output in this format:

TREND NAME:
(viral aesthetic name)

VIRAL SCORE:
(out of 100 with short reason)

AI PHOTO EDITING PROMPT:
Write a highly detailed cinematic prompt for AI image generation.

WHY IT WILL GO VIRAL:
(short explanation)

CAPTION:
(instagram-ready caption)

HASHTAGS:
(10–15 trending hashtags)

Rules:

- Make it cinematic
- Make it ultra realistic
- Make it Instagram viral style
  """

response = requests.post(
"https://openrouter.ai/api/v1/chat/completions",
headers={
"Authorization": f"Bearer {OPENROUTER_API_KEY}",
"Content-Type": "application/json"
},
json={
"model": "deepseek/deepseek-chat-v3-0324:free",
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

telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
telegram_url,
data={
"chat_id": CHAT_ID,
"text": message
}
)

print("Message sent successfully")
