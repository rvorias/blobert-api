import json
from math import log2

from data import codes_data

traits_classes = codes_data["format"]

# first pass, collect statistics
stats = {}
for trait_class in traits_classes:
    stats[trait_class] = {}

for code in codes_data["data"]:
    if code is None:
        continue
    for code_idx, code_value in enumerate(code):
        trait_class = traits_classes[code_idx]

        if code_value not in stats[trait_class]:
            stats[trait_class][code_value] = 1
        else:
            stats[trait_class][code_value] += 1

# second, convert counts to log rarity
for trait_class in stats:
    total = sum(stats[trait_class].values())
    for code_value in stats[trait_class]:
        stats[trait_class][code_value] /= total
        stats[trait_class][code_value] = -log2(stats[trait_class][code_value])

# for each code, calculate rarity
blobert_rarity = {}
for i, code in enumerate(codes_data["data"]):
    if code is None:
        blobert_rarity[i] = 0
        continue
    rarity = 0
    for code_idx, code_value in enumerate(code):
        trait_class = traits_classes[code_idx]
        rarity += stats[trait_class][code_value]
    blobert_rarity[i] = rarity

min_rarity = None
for idx, rarity in blobert_rarity.items():
    if rarity == 0:
        continue
    if min_rarity is None:
        min_rarity = rarity
    if rarity < min_rarity:
        min_rarity = rarity

sorted_rarity = sorted(blobert_rarity.items(), key=lambda x: x[1], reverse=True)

# # substract min_rarity from all rarities and turn 0 rarities to None
# for i, (idx, rarity) in enumerate(sorted_rarity):
#     if rarity == 0:
#         sorted_rarity[i] = (idx, None)
#     else:
#         sorted_rarity[i] = (idx, round(rarity - min_rarity, 2))

bucket_pop = [5, 27, 139, 737, 3893, 43]
bucket_idx = 0

for i, (idx, rarity) in enumerate(sorted_rarity):
    if bucket_pop[bucket_idx] > 0:
        sorted_rarity[i] = (idx, rarity, bucket_idx)
        bucket_pop[bucket_idx] -= 1
    else:
        bucket_idx += 1
        bucket_pop[bucket_idx] -= 1
        sorted_rarity[i] = (idx, rarity, bucket_idx)

print(bucket_pop)

# slightly alternative format
alternative_list = [None] * len(sorted_rarity)
for idx, rarity, bucket_idx in sorted_rarity:
    alternative_list[idx] = (round(rarity, 2), bucket_idx)

if __name__ == "__main__":
    with open("data/rarity.json", "w") as f:
        json.dump(sorted_rarity, f, indent=4)

    with open("data/rarity_alternative.json", "w") as f:
        json.dump(alternative_list, f, indent=4)

    with open("data/rarity_alternative_compact.json", "w") as f:
        json.dump(alternative_list, f)

    # add to codes_compact

    with open("data/codes_compact.json", "r") as f:
        codes_compact = json.load(f)

    codes_compact["format"].extend(["rarity", "rarity_bucket"])
    for idx, code in enumerate(codes_compact["data"]):
        if code is not None:
            code.extend(alternative_list[idx])

    with open("data/codes_compact_rarity.json", "w") as f:
        json.dump(codes_compact, f)
