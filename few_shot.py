from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    client = OpenAI()

    prompt = [
    # System prompt forces the format
    {"role": "system", "content": """You must strictly follow this exact format:
    option 1 for [country]: [restaurant name]
    option 2 for [country]: [restaurant name]
    option 3 for [country]: [restaurant name]

    No extra text. No bold. No numbering. Only 3 options."""},

    # Example 1
    {"role": "user", "content": "suggest european restaurant names"},
    {"role": "assistant", "content": """option 1 for italy: La Bella Roma
    option 2 for france: Paris Bistro
    option 3 for spain: Casa Madrid"""},

    # Example 2
    {"role": "user", "content": "suggest american restaurant names"},
    {"role": "assistant", "content": """option 1 for usa: Texas Grill
    option 2 for mexico: Casa Fiesta
    option 3 for brazil: Rio Kitchen"""},

    # Real question
    {"role": "user", "content": "suggest european restaurant names"},
]
    
    response = client.chat.completions.create(model = "gpt-4o-mini", messages= prompt)
    return response.choices[0].message.content
    

answer = main()
print(answer)