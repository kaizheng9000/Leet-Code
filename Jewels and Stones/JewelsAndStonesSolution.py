from itertools import count

jewels1 = "aA"
stones1 = "aAAbbbb"

jewels2 = "z"
stones2 = "ZZ"

def count_jewels(jewels, stones):
    jewel_set = set(jewels)
    num_jewels = 0

    for stone in stones:
        if stone in jewel_set:
            num_jewels += 1

    return num_jewels

print(count_jewels(jewels1, stones1))
print(count_jewels(jewels2, stones2))
