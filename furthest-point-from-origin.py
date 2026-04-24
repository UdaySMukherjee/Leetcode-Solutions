class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = r = d = 0
        for c in moves:
            if c == 'L':
                l += 1
            elif c == 'R':
                r += 1
            else:
                d += 1
        return abs(l - r) + d
