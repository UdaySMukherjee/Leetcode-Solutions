
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If we encounter a duplicate character, move the left pointer to the right
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set and update max_length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
