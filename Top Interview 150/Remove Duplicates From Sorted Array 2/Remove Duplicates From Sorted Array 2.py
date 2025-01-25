from typing import List

def removeDuplicates(nums: List[int]) -> int:

    currPos = 1
    uniqueCount = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            uniqueCount = 0
            nums[currPos] = nums[i]
            currPos += 1
        else:
            uniqueCount += 1
            if uniqueCount <= 1:
                nums[currPos] = nums[i]
                currPos += 1

    return currPos


example = [1,1,1,2,2,3]
print(removeDuplicates(example))