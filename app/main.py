import streamlit as st
from llm_service import generate_outfit, describe_clothing_item
from wardrobe_service import init_db, add_item, get_all_items
import streamlit as st
from image_service import save_image

st.title("👗 Virtual Wardrobe")

uploaded_file = st.file_uploader("Upload a clothing item", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image_path = save_image(uploaded_file)

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.success(f"Saved to: {image_path}")


if __name__ == "__main__":
    init_db()
    wardrobe = get_all_items()
    user_request = "I have a semi-formal dinner tonight, 10°C outside."
    print("Generating outfit...\n")
    result = generate_outfit(user_request, wardrobe)
    print(result)