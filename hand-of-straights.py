class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = defaultdict(int)
        for card in hand:
            count[card] += 1

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = heapq.heappop(min_heap)
            if count[start] == 0:
                continue

            for i in range(groupSize):
                card = start + i
                if count[card] == 0:
                    return False
                count[card] -= 1

                if count[card] > 0 and card not in min_heap:
                    heapq.heappush(min_heap, card)

        return True
