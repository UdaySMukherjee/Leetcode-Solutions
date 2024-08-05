class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for word, count in Counter(arr).items():
            if count == 1:
                k -= 1
                if not k:
                    return word
        return ""
