class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        Z = []
        O = []
        
        n = len(s)
        i = 0
        
        blocks = []
        while i < n:
            char = s[i]
            count = 0
            while i < n and s[i] == char:
                count += 1
                i += 1
            blocks.append((char, count))
            
        for char, count in blocks:
            if char == '0':
                Z.append(count)
            elif char == '1':
                if len(Z) > 0:  
                    O.append(count)
                    
        if blocks and blocks[-1][0] == '1' and len(O) > 0:
            O.pop()

        m = len(Z)
        
        if m < 2:
            return initial_ones
            
        top_Z = []
        for idx, val in enumerate(Z):
            top_Z.append((val, idx))
            top_Z.sort(reverse=True)
            if len(top_Z) > 3:
                top_Z.pop()
                
        max_ones = initial_ones
        
        for i in range(m - 1):
            net_gain_a = Z[i] + Z[i+1]
            
            best_other_Z = 0
            for val, idx in top_Z:
                if idx != i and idx != i + 1:
                    best_other_Z = val
                    break
            net_gain_b = best_other_Z - O[i]
            
            max_ones = max(max_ones, initial_ones + net_gain_a, initial_ones + net_gain_b)
            
        return max_ones
