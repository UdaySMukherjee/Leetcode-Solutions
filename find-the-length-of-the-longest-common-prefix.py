class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefix = {}

        # Store all prefixes of the first array
        for val in arr1:
            num = val
            while num > 0:
                if num not in prefix:
                    prefix[num] = 0
                prefix[num] += 1
                num //= 10

        # Variable to track the maximum length
        mx = float('-inf')

        # Instead of creating another map, check the prefix at the moment
        for val in arr2:
            num = val
            # Count the number of digits in num
            length = len(str(num))

            # Generate all prefixes again
            while num > 0:
                # If prefix found, break
                if num in prefix:
                    break
                num //= 10
                # Decrease digit count as we decrease prefix
                length -= 1

            mx = max(mx, length)

        return mx
