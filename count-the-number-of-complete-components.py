class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            vertices.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                vertices = []
                dfs(i)

                k = len(vertices)
                edge_count = sum(len(graph[v]) for v in vertices) // 2

                if edge_count == k * (k - 1) // 2:
                    ans += 1

        return ans
