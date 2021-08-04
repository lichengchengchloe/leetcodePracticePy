# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/decode-string/

def decodeString( s):
    """
    :type s: str
    :rtype: str
    """
    stack = [] #[]嵌套关系适合用 stack 来描述
    res = ''
    multi = 0
    for c in s:
        if '0'<= c <= '9':
            multi = multi*10+int(c)
        elif c=='[':
            stack.append((multi,res))
            multi = 0
            res = ''
        elif c==']':
            cur_multi,cur_res = stack.pop()
            res = cur_res + cur_multi*res
        else:
            res += c

    return res

s = "3[a2[c]]"
print(decodeString(s))
