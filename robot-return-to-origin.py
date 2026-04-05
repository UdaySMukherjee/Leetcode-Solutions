class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        if (count['L'] == count['R']) and (count['U'] == count['D']):
            return True
        return False
