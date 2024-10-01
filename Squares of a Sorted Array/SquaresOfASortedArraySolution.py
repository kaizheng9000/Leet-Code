

def sortedSquares(nums):
    result = []
    left = 0
    right = len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            squared = pow(nums[left], 2)
            left += 1
        else:
            squared = pow(nums[right], 2)
            right -= 1

        result.append(squared)

    result.reverse()

    return result

example = [-4,-1,0,3,10]

print(sortedSquares(example))
