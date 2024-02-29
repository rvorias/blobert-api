from io import BytesIO
from fastapi import FastAPI, Path, Depends
from fastapi.responses import StreamingResponse

from src.traits import _get_traits, _get_rarity, _get_frame_id
from src.byte_data import compose_traits, get_frame

DEBUG = True

app = FastAPI()


def common_id_param(id: int = Path(..., title="blobert id", ge=1, le=4844)):
    return id


@app.api_route("/traits/{id}", methods=["GET", "HEAD"])
def traits(id: int = Depends(common_id_param)) -> dict:
    return _get_traits(id - 1)


@app.api_route("/rarities/{id}", methods=["GET", "HEAD"])
def rarities(id: int = Depends(common_id_param)) -> float:
    return _get_rarity(id - 1)


@app.api_route("/frames/{id}", methods=["GET", "HEAD"])
def frames(id: int = Depends(common_id_param)) -> StreamingResponse:
    frame_id = _get_frame_id(id - 1)
    if frame_id is None:
        return StreamingResponse(b"")
    else:
        image_bytes = get_frame(frame_id)
        return StreamingResponse(image_bytes, media_type="image/png")


@app.api_route("/images/{id}", methods=["GET", "HEAD"])
def get_image(id: int = Depends(common_id_param)) -> StreamingResponse:
    traits = _get_traits(id - 1)

    composed_image = compose_traits(traits)

    if DEBUG:
        composed_image.save("composed.png")

    img_byte_arr = BytesIO()
    composed_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    # Return the image in the response
    return StreamingResponse(img_byte_arr, media_type="image/png")
