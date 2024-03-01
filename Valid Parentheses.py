class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        parenthesis={'(':')','{':'}','[':']'}
        for i in s:
            if i in parenthesis.keys():
                stack.append(i)
            elif i in parenthesis.values():
                if not stack or stack.pop(-1) != [key for key,
                value in parenthesis.items() if value == i][0]:
                    return False
            else:
                return False
        return len(stack)==0

        
