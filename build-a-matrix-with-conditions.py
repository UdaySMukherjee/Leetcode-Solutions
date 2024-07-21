class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologicalSort(condition):
            indegree = {i: 0 for i in range(1, k + 1)}
            adj = defaultdict(list)
            for src, des in condition:
                adj[src] += [des]
                indegree[des] += 1
            queue = []
            for i, degree in indegree.items():
                if degree == 0:
                    queue += [i]
            visited = []
            while queue:
                curr = queue.pop(0)
                visited += [curr]
                for neigh in adj[curr]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        queue += [neigh]
            return visited
        row_order = topologicalSort(rowConditions)
        col_order = topologicalSort(colConditions)
        if len(row_order) < k or len(col_order) < k:
            return []

        res = [[0 for _ in range(k)] for _ in range(k)]
        for i, row_val in enumerate(row_order):
            j = col_order.index(row_val)
            res[i][j] = row_val

        return res      
