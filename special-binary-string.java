class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def decompose(s):
            i, count = 0, 0
            res = []
            for j in range(len(s)):
                count += 1 if s[j] == '1' else -1
                if count == 0:
                    res.append('1' + decompose(s[i+1:j]) + '0')
                    i = j + 1
            res.sort(reverse=True)
            return ''.join(res)
        
        return decompose(s)
