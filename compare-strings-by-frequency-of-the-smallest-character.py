from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            smallest = min(s)
            return s.count(smallest)

        wf = sorted(f(w) for w in words)
        n = len(wf)

        return [n - bisect.bisect_right(wf, f(q)) for q in queries]
