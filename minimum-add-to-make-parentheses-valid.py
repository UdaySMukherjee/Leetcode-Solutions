class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lvl = 0
        min_lvl = 0
        for c in s:
            if c == '(':
                lvl += 1
            else:
                lvl -= 1
                min_lvl = min(min_lvl, lvl)
        moves = 0
        if min_lvl < 0:
            lvl += -min_lvl
            moves += -min_lvl
        return moves + lvl
