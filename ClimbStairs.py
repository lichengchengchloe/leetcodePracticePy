# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/climbing-stairs/
def climbStairs( n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[i]



print(climbStairs(3))
