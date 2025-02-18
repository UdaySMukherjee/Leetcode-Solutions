class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1

        # define dependencies between indices
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for i, v in enumerate(pattern):
            if v == 'I':
                adj[i].append(i + 1)
                indegree[i + 1] += 1
            
            else:
                adj[i + 1].append(i)
                indegree[i] += 1

        q = []
        for i in range(n):
            if indegree[i] == 0:
                heappush(q, i)

        # pick the smallest index out of the indices which have 
        # indegree 0, and assign the the next digit to it, 
        # decrease indegree of neighbours        
        res = [-1 for i in range(n)]
        digit = 1
        while q:
            nextIndex = heappop(q)
            res[nextIndex] = digit
            digit += 1

            for neighbour in adj[nextIndex]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    heappush(q, neighbour)
        
        return ''.join([str(v) for v in res])


        
