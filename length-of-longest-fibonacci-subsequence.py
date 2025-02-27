class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        arr.sort()
        max_len = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                left, right, temp_len = arr[i], arr[j], 0
                while left + right in num_set:
                    temp_len += 1
                    left, right = right, left + right
                max_len = max(max_len, temp_len + 2)

        return max_len if max_len > 2 else 0
