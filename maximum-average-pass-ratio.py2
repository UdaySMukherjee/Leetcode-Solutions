import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        def gain(pass_count, total_count):
            return (pass_count + 1) / (total_count + 1) - pass_count / total_count

        # Max heap, Python heapq is min-heap so we store negative gains
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        while extraStudents > 0:
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))
            extraStudents -= 1

        return sum(p / t for _, p, t in heap) / len(classes)
