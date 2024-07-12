class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substrings(s, sub, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == sub:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return "".join(stack), score

        if x >= y:
            # Prioritize "ab"
            s, score1 = remove_substrings(s, "ab", x)
            s, score2 = remove_substrings(s, "ba", y)
        else:
            # Prioritize "ba"
            s, score1 = remove_substrings(s, "ba", y)
            s, score2 = remove_substrings(s, "ab", x)
        
        return score1 + score2

