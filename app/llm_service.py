import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

"""
def test_connection():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello in a stylish way."}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
"""


def generate_outfit(user_request, wardrobe_items):
    # Convert DB rows into readable format
    wardrobe_text = ""
    for item in wardrobe_items:
        wardrobe_text += f"- {item[1]} ({item[2]}, {item[3]}, {item[4]}, {item[5]})\n"

    # Load system prompt
    with open("prompts/stylist_prompt.txt", "r") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"""
User request:
{user_request}

Available wardrobe items:
{wardrobe_text}
"""
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content
