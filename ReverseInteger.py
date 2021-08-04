# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/reverse-integer/

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    res = 0
    while x!=0:
        # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
        tmp = x%10
        if x<0 and tmp>0:
            tmp = tmp-10
        # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
        x = (x-tmp)//10
        if (res==214748364 and tmp>7) or (res>214748364):
            return 0
        if (res==-214748364 and tmp<-8) or (res<-214748364):
            return 0
        res = res*10 + tmp
    return res
x = 0
print(reverse(x))
