class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary) # Store dictionary in a set for fast lookup
        n = len(s)
        dp = [n] * (n + 1) # DP array initialized with maximum extra characters
        dp[0] = 0 # No extra characters for an empty string

        # Iterate through each index in the string
        for i in range(1, n + 1):
            # Try all substrings ending at i
            for j in range(i):
                sub = s[j:i] # Get substring s[j:i]
                if sub in dict_set:
                    dp[i] = min(dp[i], dp[j]) # If substring found in dictionary
            dp[i] = min(dp[i], dp[i - 1] + 1) # Consider current character as extra

        return dp[n] # Return the result from dp[n]
