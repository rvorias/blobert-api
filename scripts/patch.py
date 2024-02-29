patches = [
    {
        "id": 514,
        "background": "blue",
        "armour": "chainmail",
        "jewelry": "gold_ring",
        "mask": "_3d_glasses",
        "weapon": "banner_of_perfection",
    },
    {
        "id": 676,
        "background": "avnu_blue",
        "armour": "leather_armour",
        "jewelry": "bronze_ring",
        "mask": "demon_crown",
        "weapon": "squid",
    },
    {
        "id": 1066,
        "background": "realms_dark",
        "armour": "divine_robe_dark",
        "jewelry": "silver_ring",
        "mask": "lords_helm",
        "weapon": "signature_banner",
    },
    {
        "id": 1228,
        "background": "terraforms",
        "armour": "kigurumi",
        "jewelry": "necklace",
        "mask": "pepe",
        "weapon": "warhammer",
    },
    {
        "id": 2072,
        "background": "orange",
        "armour": "divine_robe",
        "jewelry": "pendant",
        "mask": "doge",
        "weapon": "ghost_wand",
    },
]

import json

from src.data import codes_data, traits_data

for patch in patches:
    for k in patch:
        code = []
        if k == "id":
            print(codes_data["data"][patch[k]])
        else:
            keys = list(traits_data[k].keys())
            index = keys.index(patch[k])
            print(index)
            code.append(index)

    codes_data["data"][patch["id"]] = code

with open("data/codes.json", "w") as f:
    json.dump(codes_data, f, indent=4)

with open("data/codes_compact.json", "w") as f:
    json.dump(codes_data, f)
