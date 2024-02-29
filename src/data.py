import os
import json
from pathlib import Path

DATA_DIR = Path("data")

with open(DATA_DIR / "codes_compact_rarity.json", "r") as f:
    codes_data = json.load(f)

with open(DATA_DIR / "traits.json", "r") as f:
    traits_data = json.load(f)

border_paths = [DATA_DIR / "frames" / name for name in os.listdir(DATA_DIR / "frames")]
border_paths.sort(reverse=True)
