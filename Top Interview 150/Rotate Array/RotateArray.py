from typing import List

def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    if k == 0: return

    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

example = [1,2,3,4,5,6,7]
rotations = 3

rotate(example, rotations)