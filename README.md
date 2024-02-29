# Blobert API

Sponsored by ![](https://glif.app/logos/logo-black-alpha.svg)

## Requirements

- python > 3.10
- [uv](https://github.com/astral-sh/uv) for venv
- [modal.com](https://modal.com/) account

## Quickstart

```shell
$ uv venv
$ uv pip install -r requirements
$ source .venv/bin/activate
```

Run locally:

```shell
$ uvicorn main:app --reload  
```

To see the docs, go to http://localhost:8000/docs

Serve temporarily

```shell
$ modal serve modal_app.py
```

Deploy

```shell
$ modal deploy modal_app.py
```

## Dev

Formatting

```shell
$ ruff format .
```

## Examples

Useful for creating derivative apps on e.g. glif:
- https://glif.app/@dham/glifs/clsypdva40001a9uooixuz3qy

## Links

- Blobert project page: https://blobert.realms.world/
- Realms project page: https://realms.world
- Glif: https://glif.app
