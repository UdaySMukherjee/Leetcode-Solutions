class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        d = [0]* (10**5+2)
        points = set()
        for left, right, color in segments:
            d[left]+=color
            d[right]-=color
            points.add(left)
            points.add(right)
        ans = []
        cur = 0
        prev = None

        for x in sorted(points):
            if prev is not None and cur != 0:
                ans.append([prev, x, cur])

            cur += d[x]
            prev = x
        return ans
