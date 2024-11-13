

def solve(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        curr = nums2[j]
        comp = nums1[i]

        if curr >= comp:
            nums1[k] = curr
            j -= 1
        else:
            nums1[k] = comp
            i -= 1

        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    print(nums1)


n1 = [4,5,6,0,0,0]
n2 = [1,2,3]
m = 3
n = 3

solve(n1, m, n2, n)