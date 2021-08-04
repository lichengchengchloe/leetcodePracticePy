# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/get-equal-substrings-within-budget/

def equalSubstring( s, t, maxCost):
    """
    :type s: str
    :type t: str
    :type maxCost: int
    :rtype: int
    """
    # 求子字符串，而不是子序列，所以使用滑动窗口
    left = 0
    sumCost = 0
    for right in range(len(s)):
        sumCost += abs(ord(s[right])-ord(t[right]))
        if sumCost > maxCost:
            sumCost -= abs(ord(s[left])-ord(t[left]))
            left += 1
    return len(s)-left

s = "abccd"
t = "bcdgf"
maxCost = 3
print(equalSubstring(s,t,maxCost))
