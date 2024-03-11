class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = defaultdict(int)
        i=0
        for j in order:
            d[j]=i
            i+=1
        print(d)

        return "".join(sorted(s, key= lambda x:d[x]))
