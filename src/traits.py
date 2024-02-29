from typing import Union

from src.data import codes_data, traits_data


def _get_traits(id: int) -> dict:
    code = codes_data["data"][id]
    if code is None:
        return {"custom": list(traits_data["custom"].keys())[id]}
    return {
        "background": list(traits_data["background"].keys())[code[0]],
        "armour": list(traits_data["armour"].keys())[code[1]],
        "jewelry": list(traits_data["jewelry"].keys())[code[2]],
        "mask": list(traits_data["mask"].keys())[code[3]],
        "weapon": list(traits_data["weapon"].keys())[code[4]],
    }


def _get_rarity(id: int) -> Union[float, None]:
    code = codes_data["data"][id]
    if code is None:
        return None
    return code[5]


def _get_frame_id(id: int) -> Union[int, None]:
    code = codes_data["data"][id]
    if code is None:
        return None
    return code[6]


if __name__ == "__main__":
    print(_get_traits(404))
    print(_get_rarity(404))
    print(_get_frame_id(404))
