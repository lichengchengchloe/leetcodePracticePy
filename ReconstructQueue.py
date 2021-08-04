# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/
def reconstructQueue( people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people.sort(key = lambda x : (-x[0],x[1]))
    i = 0
    while i<len(people) :
        if i>people[i][1]:
            # 遍历到第 i 个位置时，前面 i 个 x[0] 都比第 i 个 x[0] 大，怎么插入只取决于 x[1] 的值
            people.insert(people[i][1],people[i])
            people.pop(i+1)
        i += 1
    return people


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))
