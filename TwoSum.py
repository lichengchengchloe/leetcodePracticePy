# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/two-sum/

# 要求 nums 必须是有序数组
def twoSumDpc(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums.sort() # 这里导致下标乱序
    i = 0
    j = len(nums)-1
    while i<j:
        sum = nums[i]+nums[j]
        if sum == target:
            return [i,j]
        elif sum < target:
            i += 1
        else:
            j -= 1
    return []

def twoSum(nums,target):
    hashMap = {}
    for i in range(len(nums)):
        hashMap[nums[i]] = i
    for i in range(len(nums)):
        j = hashMap.get(target-nums[i])
        if j is not None and j!=i:
            return [i,j]
    return []

nums = [2,5,5,11]
target = 10

print(twoSum(nums,target))
