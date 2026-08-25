class Solution:
    def missingMultiple(self, a: List[int], k: int) -> int:
        a = {*a}
        return next(v for v in count(k,k) if v not in a)
