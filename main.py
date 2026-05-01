import requests

TOKEN = "8669023960:AAEw3DZdH2RhCK3WvRg3_fdYImafG0QKrrk"
CHAT_ID = "7008909688"
OPENROUTER_API_KEY = "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"

prompt = """
You are an Instagram AI Trend Predictor.

Give:

1. Viral Instagram AI photo trend (today)
2. Short explanation why it will go viral
3. Ultra cinematic AI image prompt
4. Caption
5. Hashtags
   """

try:
    prompt = """
    Give today's viral Instagram AI editing trend.
    """

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()

    if "choices" in data:
        message = data["choices"][0]["message"]["content"]
    else:
        message = str(data)

except Exception as e:
    message = str(e)
