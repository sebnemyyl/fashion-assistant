from llm_service import generate_outfit, describe_clothing_item
from wardrobe_service import init_db, add_item, get_all_items

"""
if __name__ == "__main__":
    print("Testing OpenAI connection...\n")
    result = test_connection()
    print(result)


init_db()


# Add example clothes (run once)
add_item("Black Slim Jeans", "bottom", "black", "casual", "all", "casual")
add_item("White Cotton Shirt", "top", "white", "minimal", "all", "semi-formal")
add_item("Beige Winter Jacket", "outerwear", "beige", "classic", "autumn", "casual")
add_item("Black Leather Boots", "shoes", "black", "edgy", "winter", "all")

print("Wardrobe items:")
items = get_all_items()

for item in items:
    print(item)
"""


init_db()

wardrobe = get_all_items()

user_request = "I have a semi-formal dinner tonight, 10°C outside."

print("Generating outfit...\n")

result = generate_outfit(user_request, wardrobe)

print(result)

# Path to your image
image_path = "data/shirt.png"

# Getting the Base64 string
base64_image = describe_clothing_item(image_path)
print("Clothing item description:", base64_image)

import streamlit as st
from image_service import save_image
from openai import OpenAI

st.title("👗 Virtual Wardrobe")

uploaded_file = st.file_uploader("Upload a clothing item", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image_path = save_image(uploaded_file)

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.success(f"Saved to: {image_path}")