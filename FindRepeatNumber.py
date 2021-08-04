# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
def findRepeatNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        while i!= nums[i]:
            if nums[nums[i]] == nums[i]:
                return nums[i]
            tmp = nums[i]
            nums[i] = nums[tmp]
            nums[tmp] = tmp
    return None


nums = [2, 3, 1, 0, 2, 5, 3]
print(findRepeatNumber(nums))
