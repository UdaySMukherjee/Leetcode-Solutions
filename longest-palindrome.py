class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        val = 0
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        for count in mp.values():
            if count % 2 != 0:
                res += count - 1
                val = 1
            else:
                res += count
        return res + val
