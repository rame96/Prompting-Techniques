from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
from openai import OpenAI  # type: ignore
from dotenv import load_dotenv

load_dotenv()

def idea():
    client = OpenAI()
    prompt = [{"role": "user", "content": "suggest one asian restaurant name and five dishes"}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=prompt)
    return response.choices[0].message.content

answer = idea()
print(answer)