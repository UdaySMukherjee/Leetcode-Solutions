class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = [0]*26

        for i in tasks:
            queue[ord(i) - ord('A')] += 1
        queue.sort(reverse = True)

        max_process = queue[0] -1
        idle = max_process * n

        for i in range(1,26):
            idle -= min(max_process, queue[i])

        idle = max(0, idle)

        return len(tasks) + idle
