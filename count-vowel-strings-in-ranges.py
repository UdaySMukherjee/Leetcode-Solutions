class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = len(words)
        temp = [0]*l
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(l):
            if words[i][0] in vowels and words[i][-1] in vowels:
                temp[i] = temp[i-1]+1
            else:
                temp[i] = temp[i-1]


        n = len(queries)
        res = [0]*n
        for i in range(n):
            q = queries[i]
            l, r = q[0], q[1]
            if l == 0:
                res[i] = temp[r]
            else:
                res[i] = temp[r]-temp[l-1]
        return res
