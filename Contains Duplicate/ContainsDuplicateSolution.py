example1 = [1,2,3,1]
example2 = [1,2,3,4]
example3 = [1,1,1,3,3,4,3,2,4,2]

def has_duplicate(nums):

    seen = set()

    for num in nums:
        if not num in seen:
            seen.add(num)
        else:
            return True

    return False

print(has_duplicate(example1))
print(has_duplicate(example2))
print(has_duplicate(example3))