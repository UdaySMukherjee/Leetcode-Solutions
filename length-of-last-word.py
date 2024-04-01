class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip().split()
        if not l:
            return 0
        return len(l[-1])
