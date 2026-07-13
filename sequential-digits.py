class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        l = str(low)
        h = str(high)
        
        w = "123456789"

        ans = []
        for i in range(len(l), len(h) + 1):
            
            for j in range(len(w)):
                if len(w) - j < i: break
                if int(low) <= int(w[j:j + i]) <= high:
                    ans.append(int(w[j:j + i]))
        
        return (ans)
                
