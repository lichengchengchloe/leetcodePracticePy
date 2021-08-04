# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    q = set()
    mapKeyToIndex = {}
    start = 0
    for i in range(len(s)):
        if q.__contains__(s[i]):
            j = mapKeyToIndex[s[i]]
            while j >= start:
                q.remove(s[j])
                j-=1
            start = mapKeyToIndex[s[i]]+1
        mapKeyToIndex[s[i]] = i
        q.add(s[i])
        max_len = max(max_len,len(q))
    return max_len


s= ''
print(lengthOfLongestSubstring(s))
