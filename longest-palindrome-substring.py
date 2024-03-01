class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = 0
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                if (s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1])>max):
                    max = len(s[i:j+1])
                    max_pal = s[i:j+1]
        return max_pal
