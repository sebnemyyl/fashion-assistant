import os
from uuid import uuid4
from PIL import Image

IMAGE_FOLDER = "data/images"

def save_image(file):
    # Ensure folder exists
    os.makedirs(IMAGE_FOLDER, exist_ok=True)

    # Generate unique filename
    file_id = str(uuid4())
    file_path = os.path.join(IMAGE_FOLDER, f"{file_id}.png")

    # Open and save image
    image = Image.open(file)
    image = image.convert("RGB")  # normalize format
    image.save(file_path)

    return file_path