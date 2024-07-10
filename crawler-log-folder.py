class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for i in logs:
            if i == "./":
                steps += 0
            elif i == "../":
                steps -= 1 if steps > 0 else 0
            else:
                steps += 1
        return steps
