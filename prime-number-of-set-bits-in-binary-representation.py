class Solution:   
    def countSetBits(self, n):
        count = 0
        while n > 0:
            rem = n % 2
            count += rem
            n //= 2
        return count
    
    def isPrime(self, n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        
        return True
    
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            num = self.countSetBits(i)
            if self.isPrime(num):
                count += 1
        
        return count
