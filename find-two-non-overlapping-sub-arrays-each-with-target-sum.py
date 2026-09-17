class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # best[i] = shortest valid subarray ending at or before i
        best = [n] * n

        ans = n + 1
        min_len = n

        left = 0
        curr = 0

        for right in range(n):
            curr += arr[right]

            # Shrink the window if the sum becomes too large
            while curr > target:
                curr -= arr[left]
                left += 1

            # Current window has sum equal to target
            if curr == target:
                length = right - left + 1

                # Try combining with a valid subarray
                # that ends before the current one starts
                if left > 0 and best[left - 1] != n:
                    ans = min(ans, length + best[left - 1])

                # Update the shortest valid subarray seen so far
                min_len = min(min_len, length)

            # Store the best length available up to this index
            best[right] = min_len

        return -1 if ans == n + 1 else ans
