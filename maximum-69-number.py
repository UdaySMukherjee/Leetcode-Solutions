class Solution:
    def maximum69Number (self, num: int) -> int:
        three10=(0, 3, 30, 300, 3000)# tuple is faster than list
        a, n, d=-1, num, 0
        while n>0:
            n, r=divmod(n, 10)
            if r==6: 
                a=d
            d+=1
        return num+three10[a+1]
