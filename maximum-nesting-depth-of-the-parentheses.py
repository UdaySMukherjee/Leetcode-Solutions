class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max1 =0
        for i in s:
            if i == '(':
                count+=1
                if count > max1:
                    max1 = count
            if i == ')':
                count-=1
        return max1
