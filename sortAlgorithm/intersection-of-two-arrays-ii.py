
def intersect(nums1, nums2):
    result = []


    if len(nums1) < len(nums2):
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result
    else:
        for num in nums2:
            if num in nums1:
                result.append(num)
                nums1.remove(num)
        return result
result = intersect([1,2,2,1], [2,2])
print(result)
