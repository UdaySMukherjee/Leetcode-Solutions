class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # build adjacency list
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(curr):
            if curr == 0:
                return [curr]
            
            visited.add(curr)
            l = []
            for e in graph[curr]:
                if e not in visited:
                    l = dfs(e)
                    if l:
                        return [curr] + l


        # first move bob, and track visited times
        bob_path = dfs(bob)
        bob_visited_times = {}
        for i, v in enumerate(bob_path):
            bob_visited_times[v] = i

        visited = set()
        def dfs_alice(curr, visit_time):
            max_amount = float('-inf')
            visited.add(curr)
            for e in graph[curr]:
                if e not in visited:
                    max_amount = max(max_amount, dfs_alice(e, visit_time + 1))

            vertex_income = amount[curr]
            if curr in bob_visited_times and bob_visited_times[curr] < visit_time:
                vertex_income = 0
            elif curr in bob_visited_times and bob_visited_times[curr] == visit_time:
                vertex_income = amount[curr] // 2
            if max_amount == float('-inf'):
                return vertex_income
            return max_amount + vertex_income

        # then move alice. if alice gets to a vertex (explored by bob) with lower visited time, then alice takes the amount
        return dfs_alice(0, 0)
