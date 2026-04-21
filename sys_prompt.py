from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main(msg):
    client = OpenAI()
    prompt = [{"role": "system", "content": "you are a math assistant answer to only maths related question"},
              {"role": "user", "content": msg}]
    response  = client.chat.completions.create(model="gpt-4o-mini", messages=prompt)
    return response.choices[0].message.content

for x in range(3):
    print("AI: how can i help you")
    msg = input("you: ")
    asw = main(msg)
    print(f"AI: {asw} \n")