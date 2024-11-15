

def removeElement(nums, val):
    k = 0
    left = 0
    right = len(nums) - 1

    while left <= right:
        curr = nums[left]
        end = nums[right]
        if curr == val:
            if end == val:  # Cannot swap to end
                right -= 1
            else:  # Can swap to end
                nums[right] = curr
                nums[left] = end
                left += 1
                right -= 1
                k += 1
        else:
            k += 1
            left += 1


    return k


nums1 = [3,2,2,3]
val1 = 3
print(removeElement(nums1, val1))

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(removeElement(nums2, val2))