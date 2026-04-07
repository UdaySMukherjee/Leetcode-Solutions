class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = False
        # Perimeter calculation: 2w + 2h - 4
        self.limit = 2 * (width + height - 2)        

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.limit        

    def getPos(self) -> List[int]:
        p = self.pos
        w, h = self.w, self.h
        
        if 0 <= p < w:
            return [p, 0]
        if w <= p < w + h - 1:
            return [w - 1, p - (w - 1)]
        if w + h - 1 <= p < 2 * w + h - 2:
            return [w - 1 - (p - (w + h - 2)), h - 1]
        # West edge
        return [0, h - 1 - (p - (2 * w + h - 3))]        

    def getDir(self) -> str:
        p = self.pos
        w, h = self.w, self.h
        
        # The origin (0,0) is special after a full loop
        if self.moved and p == 0:
            return "South"
        
        if 0 < p < w:
            return "East"
        if w <= p < w + h - 1:
            return "North"
        if w + h - 1 <= p < 2 * w + h - 2:
            return "West"
        if 2 * w + h - 2 <= p < self.limit:
            return "South"
        
        return "East" # Initial state        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
