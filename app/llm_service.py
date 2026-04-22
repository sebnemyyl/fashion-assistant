import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import base64

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

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")



def describe_clothing_item(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                {"type": "text", "text": "Describe this clothing item. Return JSON with type, color, style, season."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
            ]
        }
    ]
    )
    return response.choices[0].message.content