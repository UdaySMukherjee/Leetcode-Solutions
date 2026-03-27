class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return all(r[i]==r[(i+k)%len(mat[0])] for i in range(len(mat[0])) for r in mat)
