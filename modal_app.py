from modal import Image, Stub, asgi_app, Mount

from main import app

DEBUG = False

stub = Stub("blobert")

image = Image.debian_slim().pip_install("Pillow")

data_mount = Mount.from_local_dir("data", remote_path="/root/data")


@stub.function(image=image, mounts=[data_mount])
@asgi_app()
def fastapi_app():
    return app
