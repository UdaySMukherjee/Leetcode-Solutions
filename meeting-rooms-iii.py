class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """

        meetings.sort( key = lambda x: x[0])
        rooms=[i for i in range(n)]
        freq=[0]*n
        meets=[]
        for i in meetings:
            while meets and meets[0][0]<=i[0]:
                end,room = heappop(meets)
                heappush(rooms,room)
            if rooms:
                room=heappop(rooms)
                heappush(meets,(i[1],room))
            else:
                end,room = heappop(meets)
                heappush(meets,(end+(i[1]-i[0]),room))
            freq[room]+=1
        m=max(freq)
        print(freq)
        for i,j in enumerate(freq):
            if j==m:
                return i
