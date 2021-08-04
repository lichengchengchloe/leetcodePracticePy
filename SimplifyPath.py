# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/simplify-path/

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    for i in path.split('/'):
        if i not in ('','.','..'):
            stack.append(i)
        elif i == '..' and stack:
            stack.pop()
    return '/'+'/'.join(stack)

path = '/a/./b/../../c/'
print(simplifyPath(path))
