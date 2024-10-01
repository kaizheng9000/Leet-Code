

def reverseString(s):
    left = 0
    right = len(s) - 1

    while left < right:
        temp_left = s[left]
        temp_right = s[right]

        s[left] = temp_right
        s[right] = temp_left

        left += 1
        right -= 1

example = "hello"

reverseString(list(example))