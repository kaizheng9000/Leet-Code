

nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

def solve(nums, target):

    diff_set = {}

    for index in range(len(nums)):
        diff = target - nums[index]
        if diff in diff_set:
            return [diff_set[diff], index]

        diff_set[nums[index]] = index


print(solve(nums1, target1))
print(solve(nums2, target2))
print(solve(nums3, target3))