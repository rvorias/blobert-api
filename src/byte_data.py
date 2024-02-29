import base64
from PIL import Image
from io import BytesIO
from functools import lru_cache

from src.data import traits_data, border_paths


@lru_cache()  # often reused
def get_image(trait_class: str, trait_name: str) -> Image:
    image_data = base64.b64decode(traits_data[trait_class][trait_name])
    return Image.open(BytesIO(image_data)).convert("RGBA")


def compose_traits(traits: dict) -> Image:
    # Create a new blank image with alpha channel
    composed_image = Image.new("RGBA", (48, 48), (0, 0, 0, 0))

    for trait_class, trait_name in traits.items():
        image = get_image(trait_class, trait_name)
        composed_image.paste(image, (0, 0), image)

    return composed_image


@lru_cache()  # often reused
def get_frame(frame_id: int) -> bytes:
    image = Image.open(border_paths[frame_id])
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return img_byte_arr


if __name__ == "__main__":
    compose_traits({"armour": "chainmail", "weapon": "dope_uzi"}).save("composed.png")
