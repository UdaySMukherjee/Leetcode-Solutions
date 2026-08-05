class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(n)}
        for src, dst in invocations:
            adj[src].append(dst)

        q = [k]
        visited = set([k])
        while q:
            suspicious = q.pop()
            for neighbor in adj[suspicious]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    
        ans = []
        for method in range(n):
            if method in visited: continue
            for neighbor in adj[method]:
                if neighbor in visited:
                    return list(range(n))
            ans.append(method)
        return ans
