# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/interleaving-string/

def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    len1 = len(s1)
    len2 = len(s2)
    len3 = len(s3)
    if len1+len2 != len3:
        return False
    # if len3 == 0:
    #     return True
    dp = [[False for j in range(len2+1)] for i in range(len1+1) ]
    dp[0][0] = True
    for i in range(1,len1+1):
        dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
    for j in range(1,len2+1):
        dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    return dp[-1][-1]

s1 = 'a'
s2 = ''
s3 = 'a'

print(isInterleave(s1,s2,s3))
