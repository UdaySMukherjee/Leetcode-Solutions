class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        maxScore = 0
        res = [0] * len(aliceArrows)
    
        def recur(i, numArrows, score, path):
            nonlocal maxScore, res
            if i >= len(aliceArrows):
                if score > maxScore:
                    if numArrows > 0:
                        path[0] += numArrows
                    res = path
                    maxScore = score
                return score
            
            notPick = recur(i+1, numArrows, score, path + [0])
            pick = 0
            if numArrows - (aliceArrows[i] + 1) >= 0:
                pick = recur(i+1, numArrows - (aliceArrows[i] + 1), score + i, path + [aliceArrows[i] + 1])
            
            return max(pick, notPick)
        recur(0, numArrows, 0, [])
        return res
