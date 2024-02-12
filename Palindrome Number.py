class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        sum=0
        while num>0:
            dig = num%10
            sum = sum*10 + dig
            num = num//10

        if sum == x:
            return True
        else: 
            return False
        