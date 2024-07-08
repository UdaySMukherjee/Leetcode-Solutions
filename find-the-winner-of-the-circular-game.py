
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        current_position = 0
        while n > 1:
            current_position = (current_position + (k-1)) % n
            friends.pop(current_position)
            n -= 1
        return friends[0]
