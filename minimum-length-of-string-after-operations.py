class Solution:
    def minimumLength(self, s: str) -> int:
        arr = [0] * 26
        
        # Counting the char
        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        
        # Applying the rules
        for i in range(26):
            while arr[i] >= 3:
                arr[i] -= 2
        
        # Counting the length of final string
        length = sum(arr)
        
        return length
