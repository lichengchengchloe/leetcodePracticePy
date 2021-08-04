
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_len = len(g)
        s_len = len(s)
        g_i = 0
        s_i = 0
        while g_i < g_len and s_i < s_len:
            if g[g_i]<=s[s_i]:
                g_i +=1
                s_i +=1
            elif g[g_i]>s[s_i]:
                s_i+=1
        return g_i


if __name__ == '__main__':
    g = [1,1]
    s = [1,2,3]
    solusion = Solution()
    print(solusion.findContentChildren(g,s))
