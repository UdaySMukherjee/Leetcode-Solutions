class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n=len(mat), len(mat[0])
        N=m*n

        to_i=[-1]*(N+1)
        to_j=[-1]*(N+1)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                to_i[x]=i
                to_j[x]=j
        R=[0]*m
        C=[0]*n
        for i, x in enumerate(arr):
            R[to_i[x]]+=1
            C[to_j[x]]+=1
            if R[to_i[x]]==n or C[to_j[x]]==m:
                return i
        return -1
