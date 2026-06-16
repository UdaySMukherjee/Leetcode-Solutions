class Solution:
    def processStr(self, s: str) -> str:

        result = ""
        for ch in s:
            if ch == '*':
                result = result[:-1]
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]
            else:
                result +=ch
                
        return result

        
