
def minStartValue(nums):
    m = s = 0
    for num in nums:
        s += num
        m = min(m, s)
    return 1 - m

    
minStartValue([-3,2,-3,4,2])