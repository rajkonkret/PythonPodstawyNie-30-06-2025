import openai
import os
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or "tu_wstaw_swoj_klucz"
client = openai.OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Jesteś nauczycielem Pythona."},
        {"role": "user", "content": "Wyjaśnij, czym jest lista w Pythonie."}
    ]
)

print(response.choices[0].message.content)
print(response.choices[0])
print(response.choices)
print(response)