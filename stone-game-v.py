class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        def f(l, r):
            if dp[l][r]:
                return dp[l][r]
            ans = 0
            for i in range(l, r):
                left = pref[i+1] - pref[l]
                right = pref[r+1] - pref[i+1]
                if left < right:
                    s = left + f(l, i)
                    if s > ans:
                        ans = s
                elif left > right:
                    s = right + f(i + 1, r)
                    if s > ans:
                        ans = s
                else:
                    ans = max(ans, left + max(f(l, i), f(i + 1, r)))
            dp[l][r] = ans
            return ans
        n = len(stoneValue)
        pref = [0]
        for stone in stoneValue:
            pref.append(pref[-1] + stone)
        pref = tuple(pref)
        dp = [[0] * n for _ in range(n)]
        return f(0, n - 1)
