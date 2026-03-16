class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n,m= len(grid), len(grid[0])
        def calcAreaForCell(x,y):
            maxSize= min(y+1, m-y, (n-x+1)//2 ) # max len of each size of rhombus
            for k in range(maxSize): # iterating from ,<=size 1<= maxSize and calculating area
                if k==0: 
                    heapq.heappush(pq,-grid[x][y]) # considering only one cell as rhombus
                    continue
                s= 0
                i,j= x,y
                for _ in range(k): # coming down-left
                    s+=grid[i][j]
                    i+=1
                    j-=1
                for _ in range(k): # coming down-right
                    s+=grid[i][j]
                    i+=1
                    j+=1
                for _ in range(k): # going up-right
                    s+=grid[i][j]
                    i-=1
                    j+=1
                for _ in range(k): # going up-left
                    s+=grid[i][j]
                    i-=1
                    j-=1
                heapq.heappush(pq,-s)
            return 
        pq=[]
        st=set()
        for i in range(n):
            for j in range(m):
                calcAreaForCell(i,j)
                
        while pq and len(st)<3: # filtering biggest unique values from priority queue
            area= -heapq.heappop(pq)
            st.add(area)
        return sorted(list(st), reverse=True)
