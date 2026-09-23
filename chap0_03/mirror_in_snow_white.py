from openai import OpenAI
from dotenv import load_dotenv # .env 찾기
import os # file이나 folder 담기 위해 필수. .env파일의 위치를 찾음

load_dotenv() # .env파일 실행
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key = api_key) # api_key를 OpenAI서버로 보내 인증 후 다시 돌아와 client에 넣어줌

# key값을 갖고 있는 client / 답변내용을 response에 저장
response = client.chat.completions.create( 
    model = "gpt-4o",
    temperature = 0.9, # 반드시 소수점 작성 0.0, 1.0 등
    messages = [
        {"role" : "system", "content" : "너는 백설공주 이야기 속의 거울이야. 그 이야기 속의 마법 거울의 캐릭터에 부합하게 답변해줘."},
        {"role" : "user", "content" : "세상에서 누가 제일 아름답니?"},
    ]

)

print(response)

print('----')
print(response.choices[0].message.content)
