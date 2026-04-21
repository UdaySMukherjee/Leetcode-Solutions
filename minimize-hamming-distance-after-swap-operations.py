class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        graph = [[] for _ in range(n)]
        for u, v in allowedSwaps:
            graph[u].append(v)
            graph[v].append(u)

        
        def dfs(node):
            visited[node] = 1
            cnt[source[node]] += 1
            cnt[target[node]] -= 1
            for neib in graph[node]:
                if not visited[neib]:
                    dfs(neib)

        ans, visited = 0, [0] * n
        for node in range(n):
            if not visited[node]:
                cnt = defaultdict(int)
                dfs(node)
                ans += sum(f for f in cnt.values() if f > 0)
        return ans
