import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet101
from PIL import Image
import numpy as np

model = deeplabv3_resnet101(pretrained=True).eval()

def remove_background(image: Image.Image) -> Image.Image:
    transform = T.Compose([
        T.Resize(512),
        T.ToTensor(),
    ])

    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)['out'][0]

    mask = output.argmax(0).byte().cpu().numpy()

    # Keep "person" class (15 in COCO)
    mask = (mask == 15).astype(np.uint8) * 255

    # Resize mask back to original image dimensions
    mask_resized = Image.fromarray(mask).resize(image.size, resample=Image.NEAREST)

    img = np.array(image.convert("RGBA"))
    img[:, :, 3] = np.array(mask_resized)

    return Image.fromarray(img)