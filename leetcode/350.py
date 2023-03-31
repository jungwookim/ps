def solution(nums1, nums2):
    d1 = {}
    d2 = {}
    for n1 in nums1:
        if n1 in d1:
            d1[n1] += 1
        else:
            d1[n1] = 1
    for n2 in nums2:
        if n2 in d2:
            d2[n2] += 1
        else:
            d2[n2] = 1

    ans = []
    for n1 in nums1:
        if n1 in nums2 and d2[n1] > 0:
            ans.append(n1)
            d2[n1] -= 1

    return ans

print(solution([1,2,2,1], [2,2]))
print(solution([4,9,5], [9,4,9,8,4]))
print(solution([1,2], [2,2]))
