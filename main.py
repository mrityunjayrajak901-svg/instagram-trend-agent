from telegram import Bot
import requests

TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"
OPENROUTER_API_KEY = "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"

bot = Bot(token=TOKEN)

prompt = """
Give today's viral Instagram AI photo editing trend.
Include:

1. Trend name
2. Viral prediction
3. Cinematic editing prompt
4. Caption
5. Hashtags
   """

response = requests.post(
url="https://openrouter.ai/api/v1/chat/completions",
headers={
"Authorization": f"Bearer {OPENROUTER_API_KEY}",
"Content-Type": "application/json"
},
json={
"model": "deepseek/deepseek-chat",
"messages": [
{"role": "user", "content": prompt}
]
}
)

data = response.json()

message = data["choices"][0]["message"]["content"]

bot.send_message(chat_id=CHAT_ID, text=message)
