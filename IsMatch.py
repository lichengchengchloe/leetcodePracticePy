# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/wildcard-matching/

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    ns = len(s)
    np = len(p)
    dp = [[False for _ in range(ns+1)] for _ in range(np+1)]
    dp[0][0] = True #开头字母为空字符

    for i in range(1,np+1):
        for j in range(ns+1):
            if p[i-1] == '*' and dp[i-1][j]:
                for r in range(j,ns+1):
                    dp[i][r]=True
                break
            elif p[i-1] == '?':
                dp[i][j]= dp[i-1][j-1] if j>0 else False
            else:
                dp[i][j]= (s[j-1]==p[i-1] and dp[i-1][j-1] if j>0 else False)
    return dp[np][ns]



s = 'adceb'
p = '*a*b'
print(isMatch(s,p))
