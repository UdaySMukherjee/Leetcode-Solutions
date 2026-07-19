class Stack:
    """My custom implemented stack"""
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, x):
        self.stack.append(x)
        self.length += 1

    def top(self):
        if self.length > 0:
            return self.stack[-1]

    def pop(self):
        if self.length > 0:
            val = self.stack[-1]
            del self.stack[-1]
            self.length -= 1
            return val

    def is_emtpy(self):
        return self.length == 0

class Solution:
    """My stack-based greedy solution"""
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        last = {}
        for i, val in enumerate(s):
            last[val] = i
        
        stack = Stack()
        used = set()
        res = ""
        
        for i in range(n):
            if s[i] in used:
                continue
            while not stack.is_emtpy() and stack.top() > s[i] and i < last[stack.top()]:
                curr = stack.pop()
                used.remove(curr)
            used.add(s[i])
            stack.push(s[i])
        
        while not stack.is_emtpy():
            res = stack.pop() + res
        return res              
