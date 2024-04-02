class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = {}
        
        for i in range(len(s)):
            if s[i] in char_map:  
                if char_map[s[i]] != t[i]:  
                    return False
            else:
                if t[i] in char_map.values(): 
                    return False
                char_map[s[i]] = t[i] 
        
        return True
