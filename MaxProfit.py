# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

def maxProfit( k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    n = len(prices)
    # k 参数可能给的很大，但是最多进行 n//2 比交易
    k = min(k,n//2)
    # 可能一笔交易都没有才是最大收益 k=0
    buys = [[0]*(k+1) for j in range(n)]
    sells = [[0]*(k+1) for j in range(n)]

    # 第 0 天之前买入和卖出都不合法
    for i in range(1,k+1):
        buys[0][i]=sells[0][i] = float("-inf")
    # 如果第 0 天买入（买入不算交易）
    buys[0][0] = -prices[0]
    # 第 0 天啥也做不，收益为 0
    sells[0][0] = 0

    for i in range(1,n):
        buys[i][0] = max(buys[i-1][0],-prices[i])
        for j in range(1,k+1):
            buys[i][j] = max(buys[i-1][j],sells[i-1][j]-prices[i])
            sells[i][j] = max(sells[i-1][j],buys[i-1][j-1]+prices[i])

    return max(sells[n-1])

k = 2
prices = []
print(maxProfit(k,prices))
