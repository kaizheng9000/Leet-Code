
def twoSum(numbers: list[int], target: int):

    left = 0
    right = len(numbers) - 1

    while left < right:
        currSum = numbers[left] + numbers[right]
        if currSum == target:
            return [left + 1, right + 1]
        elif currSum > target:
            right -= 1
        else:
            left += 1


example = [2,7,11,15]
toFind = 9

example2 = [2,3,4]
toFind2 = 6

example3 = [-1,0]
toFind3 = -1

print(twoSum(example, toFind))
print(twoSum(example2, toFind2))
print(twoSum(example3, toFind3))
