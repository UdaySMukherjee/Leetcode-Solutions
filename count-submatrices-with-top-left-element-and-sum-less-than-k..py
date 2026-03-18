class Solution:
    def countSubmatrices(self, v, k):
        n, m = len(v), len(v[0])

        for i in range(n):
            for j in range(1, m):
                v[i][j] += v[i][j - 1]

        for i in range(m):
            for j in range(1, n):
                v[j][i] += v[j - 1][i]

        ans = 0
        for i in range(n):
            for j in range(m):
                if v[i][j] <= k:
                    ans += 1

        return ans
