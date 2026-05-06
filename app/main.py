import os
from uuid import uuid4
 
import streamlit as st
from PIL import Image
 
from image_service import remove_background
from llm_service import describe_clothing_item, generate_outfit
from wardrobe_service import add_item, get_all_items, init_db
 
 
IMAGE_FOLDER = "data/images"
 
init_db()
 
st.title("👗 Virtual Wardrobe")
 
uploaded_file = st.file_uploader("Upload a clothing item", type=["png", "jpg", "jpeg"])
 
if uploaded_file is not None:
    image = Image.open(uploaded_file)
 
    with st.spinner("Removing background..."):
        image_no_bg = remove_background(image)
 
    # Save the background-removed image as PNG (preserves transparency)
    os.makedirs(IMAGE_FOLDER, exist_ok=True)
    file_id = str(uuid4())
    image_path = os.path.join(IMAGE_FOLDER, f"{file_id}.png")
    image_no_bg.save(image_path, format="PNG")
 
    st.image(image_no_bg, caption="Background removed", use_container_width=True)
 
    with st.spinner("Analysing clothing item..."):
        item_info = describe_clothing_item(image_path)
 
    if item_info:
        st.subheader("Detected item")
        st.json(item_info)
 
        add_item(
            name=f"{item_info.get('color', '')} {item_info.get('type', 'item')}".strip(),
            type_=item_info.get("type", ""),
            color=item_info.get("color", ""),
            style=item_info.get("style", ""),
            season=item_info.get("season", ""),
            occasion=item_info.get("occasion", ""),
            image_path=image_path,
        )
        st.success("Item added to your wardrobe!")
    else:
        st.error("Could not analyse the clothing item. Please try a clearer photo.")
 
 
if __name__ == "__main__":
    wardrobe = get_all_items()
    user_request = "I have a semi-formal dinner tonight, 10°C outside."
    print("Generating outfit...\n")
    result = generate_outfit(user_request, wardrobe)
    print(result)