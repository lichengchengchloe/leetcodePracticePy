# -*- coding: UTF-8 -*-

def yanghui(n):
    """
     :type n: int
     """
    if n == 0 or n is None:
        print('')
    l = [1]
    print(l[0])
    cur = 1
    while cur<=n:
        l.append(0)
        l = [l[i-1] + l[i] for i in range(len(l))]
        if cur !=1:
            tmp = [str(l[i]) for i in range(len(l))]
            # tmp = []
            # for i in range(len(l)):
            #     tmp.append(str(l[i]))
            print(' '.join(tmp))
        cur += 1

yanghui(5)
