class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # prevent overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = 0
        if dividend < 0:
            sign += 1
            dividend = abs(dividend)
        if divisor < 0:
            sign += 1
            divisor = abs(divisor)
        
        res = 0
        while dividend >= divisor:
            value = divisor
            multiple = 1

            while dividend >= value + value:
                value += value
                multiple += multiple
            
            dividend -= value
            res += multiple
        
        return -res if sign == 1 else res
