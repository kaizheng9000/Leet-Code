example = [3,2,3]
example2 = [2,2,1,1,1,2,2]

# Time: O(n) Space: O(n)
def find_freq(nums):

    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return max(freq, key=lambda x: freq[x])


# Time: O(n) Space: O(1)
def find_freq_in_place(nums):

    ans = -1
    count = 0

    for num in nums:
        if count == 0:
            ans = num

        if num == ans:
            count += 1
        else:
            count -= 1

    return ans


print(find_freq(example))
print(find_freq(example2))

print(find_freq_in_place(example))
print(find_freq_in_place(example2))