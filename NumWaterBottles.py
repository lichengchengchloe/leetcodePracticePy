# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/water-bottles/

def numWaterBottles( numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """

    # 模拟
    # n = numBottles
    # while numBottles >= numExchange:
    #     numBottles -= numExchange
    #     numBottles += 1
    #     n += 1
    # return n
    # 数学
    return  (numBottles-numExchange)//(numExchange-1)+1+numBottles if numBottles >= numExchange else numBottles

print(numWaterBottles(15,4))
