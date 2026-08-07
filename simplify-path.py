class Solution:
    def simplifyPath(self, path: str) -> str:
        comps = path.split('/')
        stack = []
        for c in comps:
            if c == '' or c == '.':
                continue
            if c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return '/' + '/'.join(stack)
                
