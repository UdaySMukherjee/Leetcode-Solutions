class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n 
        for i in favorite:
            deg[i] += 1

        q = deque()
        
        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        chain = [1] * n
        d = 1
        while q:
            Que = len(q)
            for _ in range(Que):
                i = q.popleft()
                j = favorite[i]
                chain[j] = max(d + 1, chain[j])
                deg[j] -= 1
                if deg[j] == 0:
                    q.append(j)
            d += 1

        maxCycle = 0
        turn = 0
        for i in range(n):
            if deg[i] == 0:
                continue
            sizeCycle = 0
            j = i
            while deg[j] != 0:
                deg[j] = 0
                sizeCycle += 1
                j = favorite[j]

            if sizeCycle > 2:
                maxCycle = max(maxCycle, sizeCycle)
            else:
                turn += chain[i] + chain[favorite[i]]
        
        return max(maxCycle, turn)
