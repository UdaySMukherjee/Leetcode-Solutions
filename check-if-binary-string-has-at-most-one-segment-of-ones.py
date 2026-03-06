class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = s.strip("0")
        return ("0" not in s)
