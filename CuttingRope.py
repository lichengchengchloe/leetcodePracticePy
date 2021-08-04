# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

def cuttingRope( n):
    """
    :type n: int
    :rtype: int
    """
    if n<4:
        return n-1
    res = 1
    # 数学推导，有最优解
    while n>4:
        res *=3
        n -= 3
    return res*n

print(cuttingRope(10))
