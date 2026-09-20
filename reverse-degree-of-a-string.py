class Solution(object):
    def reverseDegree(self, s):
        an = 0
        n = len(s)
        for i in range(n):
            x = 26 - (ord(s[i]) - ord('a'))
            an += (i + 1) * x
        return an
        
