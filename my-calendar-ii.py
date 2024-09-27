from sortedcontainers import SortedSet

class MyCalendarTwo:

    def __init__(self):
        self.first_book_start = SortedSet()
        self.first_book_end = SortedSet()
        self.second_book_start = SortedSet()
        self.second_book_end = SortedSet()

        

    def book(self, start: int, end: int) -> bool:
        insert = True
        fs = set()
        fe = set()
        ss = set()
        se = set()
        while insert and start != end:
            insert = False
            idx = self.first_book_start.bisect_left(end)
            
            curr_end = self.first_book_end[idx - 1] if idx >= 1 else float('-inf')
            new_end = max(curr_end, start)
            if new_end < end:
                fs.add(new_end)
                fe.add(end)
                end = new_end
                insert = True

        
            idx = self.second_book_start.bisect_left(end)
            curr_end = self.second_book_end[idx - 1] if idx >= 1 else float('-inf')
            new_end = max(curr_end, start)
            if new_end < end:
                ss.add(new_end)
                se.add(end)
                end = new_end
                insert = True

            if end == start:
                for e in fs:
                    self.first_book_start.add(e)
                for e in fe:
                    self.first_book_end.add(e)
                for e in ss:
                    self.second_book_start.add(e)
                for e in se:
                    self.second_book_end.add(e)
                return True
        return False

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
