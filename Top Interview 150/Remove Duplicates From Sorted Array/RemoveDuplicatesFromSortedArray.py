from typing import List


def removeDuplicates(nums: List[int]) -> int:
    current = 0
    currUnique = nums[0]
    duplicate = 1
    k = 1

    while duplicate < len(nums):
        # If they are the same, move dup pointer and check next value
        if nums[duplicate] == currUnique:
            duplicate += 1
            continue
        else:  # If they are not the same, then we can move the current pointer
            nums[current + 1] = nums[duplicate]
            currUnique = nums[duplicate]
            k += 1
            current += 1

    return k


nums = [1,1,2]
print(removeDuplicates(nums))