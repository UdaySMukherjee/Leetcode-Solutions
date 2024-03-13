class Solution:
    def pivotInteger(self, n: int) -> int:
        i=1
        j=n
        while(i<=j):
            mid = j + (i-j)//2
            Left = mid*(mid+1)//2
            Right = n*(n+1)//2 - Left + mid
            print(Left,Right,mid)
            if(Left==Right):
                return mid
            elif(Left<Right):
                i = mid + 1
            else:
                j = mid - 1
        return -1



