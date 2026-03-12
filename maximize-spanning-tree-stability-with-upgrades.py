class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = [i for i in range(n)]

        def find_parent(x):
            if x != parent[x]:
                parent[x] = find_parent(parent[x])
            return parent[x]

        mini = 10**9
        non_edges = []
        for u, v, s, must in edges:
            if must == 1:
                u_p = find_parent(u)
                v_p = find_parent(v)
                if u_p == v_p:
                    return -1
                parent[u_p] = parent[v_p]
                mini = min(mini, s)
            else:
                non_edges.append([u, v, s])

        non_edges.sort(key = lambda x: -x[2])
        pq = []
        for u, v, s in non_edges:
            u_p = find_parent(u)
            v_p = find_parent(v)
            if u_p != v_p:
                parent[u_p] = parent[v_p]
                heappush(pq, s)
                
        mp = set()
        for i in range(n):
            x = find_parent(i)
            if x not in mp:
                if len(mp) == 0:
                    mp.add(x)
                else:
                    return -1
                    
        ansx = []
        while k and len(pq):
            x = heappop(pq)
            x = x*2
            ansx.append(x)
            k-=1
        while len(pq):
            ansx.append(heappop(pq))
        return min(mini, (min(ansx) if ansx else 10**9))


        
                
                
