from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key = api_key)

while True : # while 뒤 조건문 작성. True 작성 시 무한루프
    user_input = input("사용자: ")

    if user_input == "exit": # if문 뒤 exit 입력 시 break로 루프 빠져나옴
        break

    response = client.chat.completions.create(
        model = "gpt-4o",
        temperature = 0.9,
        messages = [
            {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
            {"role": "user", "content": user_input},
        ],
    )
    print("AI: " + response.choices[0].message.content)
