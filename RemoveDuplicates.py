# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n==0:
        return 0
    # 有序数组的重复项肯定是挨在一起的，将不重复的数字赋值到重复项即可
    p = 0
    q = 1
    while q<n:
        if nums[p]!=nums[q]:
            p += 1
            # 如果 p==q 也不需要赋值
            nums[p]=nums[q]
        q += 1
    return len(nums[0:p+1])


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
