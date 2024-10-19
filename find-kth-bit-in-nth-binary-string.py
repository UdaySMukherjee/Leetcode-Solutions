class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        length = (1 << n) - 1
        mid = length // 2 + 1
        return self.findKthBit(n - 1, k) if k < mid else '1' if k == mid else self.invert(self.findKthBit(n - 1, length - k + 1))
    def invert(self, c: str) -> str:
        return '1' if c == '0' else '0' 
