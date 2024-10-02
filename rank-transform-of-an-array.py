class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return [rank[x] for x in arr] if(rank:={x:i+1 for i,x in enumerate(sorted(set(arr)))}) else []
      
