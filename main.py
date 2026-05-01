import requests

TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"

prompt = """
Give one viral Instagram AI photo editing trend.
Include:

1. Trend Name
2. Cinematic Prompt
3. Caption
4. Hashtags
   """

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

response = requests.post(
API_URL,
json={
"inputs": prompt
}
)

data = response.json()

message = str(data)

requests.post(
f"https://api.telegram.org/bot{TOKEN}/sendMessage",
data={
"chat_id": CHAT_ID,
"text": message[:3500]
}
)

print("Done")
