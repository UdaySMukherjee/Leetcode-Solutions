class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_with_index = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        
        # Initialize the result list with the appropriate size
        res = [""] * len(score)
        
        # Assign ranks or medals based on the sorted order
        for rank, (_, idx) in enumerate(score_with_index):
            if rank == 0:
                res[idx] = "Gold Medal"
            elif rank == 1:
                res[idx] = "Silver Medal"
            elif rank == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank + 1)
        
        return res
