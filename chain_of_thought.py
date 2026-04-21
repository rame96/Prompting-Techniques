from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
from openai import OpenAI  # type: ignore
from dotenv import load_dotenv

load_dotenv()

def idea():
    client = OpenAI()
    prompt = [{"role": "user", "content": """suggest one asian restaurant name and five dishes.
               
                Think step by step:
                1. First decide the country (Chinese, Japanese, Thai, etc.)
                2. Then pick a fitting restaurant name
                3. Then choose dishes that match that cuisine"""}
             ]
    response = client.chat.completions.create(model="gpt-5-nano", messages=prompt)
    return response.choices[0].message.content

answer = idea()
print(answer)