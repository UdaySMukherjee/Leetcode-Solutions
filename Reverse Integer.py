class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        num = x
        rev = 0
        if num < 0:
            num = abs(num)
            while num > 0:
                dig = num % 10
                rev = rev * 10 + dig
                num = num // 10
            rev *= -1
        else:
            while num > 0:
                dig = num % 10
                rev = rev * 10 + dig
                num = num // 10
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev