# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
import collections

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = []
    deque = collections.deque()
    n = len(nums)
    for i,j in zip(range(1-k,n+1-k),range(n)):
        if i>0 and nums[i-1]==deque[0]:
            deque.popleft()
        while deque and deque[-1]<nums[j]:
            deque.pop()
        deque.append(nums[j])
        if i>=0:
            res.append(deque[0])
    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))
