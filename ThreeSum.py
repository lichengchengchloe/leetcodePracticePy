# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/3sum/
def threeSum( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums or len(nums)<3:
        return []
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if nums[i]>0:
            return res
        # 如果和上一步的值相同，则不用再重复遍历
        if i > 0 and nums[i]==nums[i-1]:
            continue
        l = i+1
        r = n-1
        while l<r:
            if nums[i]+nums[l]+nums[r] == 0:
                res.append([nums[i],nums[l],nums[r]])
                while l<n-1 and nums[l]==nums[l+1]:
                    l+=1
                while r>0 and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
            elif nums[i]+nums[l]+nums[r] > 0:
                r-=1
            else:
                l+=1
    return res

nums = [0,0,0]
print(threeSum(nums))
