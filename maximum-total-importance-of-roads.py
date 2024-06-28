class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        Arr = [0] * n
        for A,B in roads:
            Arr[A] += 1 
            Arr[B] += 1
        Arr.sort() 
        summ = 0
        for i in range(len(Arr)):
            summ += Arr[i] * (i+1)  
        
        return summ
