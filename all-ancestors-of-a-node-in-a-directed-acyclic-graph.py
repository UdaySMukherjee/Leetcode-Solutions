class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indegree = [0] * n

        for x, y in edges:
            adj[x].append(y)
            indegree[y] += 1
        
        queue = deque()
        parent = defaultdict(set)

        for i in range(n):
            if indegree[i] == 0:
                queue.append([i, set()])
        
        while queue:
            node, node_parent = queue.popleft()
            for adj_n in adj[node]:
                indegree[adj_n] -= 1
                parent[adj_n].add(node)
                parent[adj_n].update(node_parent)
                if indegree[adj_n] == 0:
                    queue.append([adj_n, parent[adj_n]])

        res = []
        for i in range(n):
            if i in parent:
                res.append(sorted(list(parent[i])))
            else:
                res.append([])
        
        return res 
