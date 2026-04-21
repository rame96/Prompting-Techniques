from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    client = OpenAI()
    prompt = [{"role": "system", "content": "Always respond in valid JSON only. No extra text."},
             {"role": "user", "content": """suggest one asian restaurant name and five dishes.
              Use this format:
             {
              "restaurant_name": "",
              "dishes": []
             }"""}]
    
    response  = client.chat.completions.create(model="gpt-4o-mini", messages=prompt)
    return response.choices[0].message.content

anw = main()
print(anw)