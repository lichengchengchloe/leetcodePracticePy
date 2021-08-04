# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/partition-equal-subset-sum/

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    if sum%2!=0:
        return False
    target = sum//2
    dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
    # 第一个物品如果重量不超过 target 则满足容量为自己的背包
    if nums[0] <= target:
        dp[0][nums[0]] = True
    # 从第二个物品开始，根据容量动态选择装入还是不装入
    for i in range(1,len(nums)):
        for j in range(target+1):
            dp[i][j] = dp[i-1][j]
            if nums[i]==j:
                dp[i][j] = True
                continue
            if nums[i]<j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
    return dp[len(nums)-1][target]
nums = [1,2,3,5]
print(canPartition(nums))
