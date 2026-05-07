class Solution:
    def maxValue(self, A: List[int]) -> List[int]:
        N = len(A)
        S = A[:]
        for i in range(N - 2, -1, -1):
            S[i] = min(S[i], S[i + 1])

        ans = []
        m = 0
        for i, x in enumerate(A):
            m = max(m, x)
            if i == N - 1 or m <= S[i + 1]:
                ans.extend([m] * (i + 1 - len(ans)))
                m = 0

        return ans
