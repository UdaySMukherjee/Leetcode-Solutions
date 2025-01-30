class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        #adj for the graph
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a-1].append(b-1)
            adj[b-1].append(a-1)

        #check each component is bipartite
        def compbipartite(adj,state,start):
            q = deque()
            q.append(start)
            state[start] = 1
            while q:
                curr = q.popleft()
                for i in adj[curr]:
                    if not state[i]:
                        state[i] = (-1) * state[curr]
                        q.append(i)
                    elif state[i] == state[curr]:
                        return False
            return True

        def checkbipartite(adj,n):
            state = [0] * n
            for i in range(n):
                if state[i] == 0 and not compbipartite(adj,state,i):
                    return False
            return True

        #finding dist from 1 node to all other nodes
        def bfs(adj,n,src):
            vis = [0] * n
            q = deque()
            q.append(src)
            vis[src] = 1
            levels = 0
            while q:
                num = len(q)
                for _ in range(num):
                    curr = q.popleft()
                    for i in adj[curr]:
                        if not vis[i]:
                            q.append(i)
                            vis[i] = 1
                levels += 1
            return levels

        def findmax(adj,max_dis,vis,src):
            q = deque()
            q.append(src)
            vis[src] = 1
            ans = 0
            while q:
                curr = q.popleft()
                ans = max(ans,max_dis[curr])
                for i in adj[curr]:
                    if not vis[i]:
                        vis[i] = 1
                        q.append(i)
            return ans

        #if not bipartite return -1
        if not checkbipartite(adj,n):
            return -1

        max_dis = [0] * n
        for i in range(n):
            max_dis[i] = bfs(adj,n,i)
        
        res = 0
        vis = [0] * n
        for i in range(n):
            if not vis[i]:
                res += findmax(adj,max_dis,vis,i)
        return res

        

        
