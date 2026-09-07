class Solution:

    def distinctSubseqII(self, s: str) -> int:

        MOD = 10 ** 9 + 7

        dp, lst = 1, [0] * 26

        for c in s:

            new_dp = (2 * dp - lst[ord(c) - ord('a')]) % MOD

            lst[ord(c) - ord('a')] = dp

            dp = new_dp

        return (dp - 1) % MOD
