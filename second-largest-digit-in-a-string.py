class Solution:
    def secondHighest(self, s: str) -> int:
        digits = list()
        for ch in s:
            if(ch.isdigit()):
                digits.append(int(ch))
        fmax,smax = -1,-1
        for index in range(len(digits)):
            if(digits[index] > fmax):
                smax = fmax
                fmax = digits[index]
            elif(digits[index] < fmax and digits[index] > smax):
                smax = digits[index]
        return smax
        
