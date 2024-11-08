class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        #bitwise XOR has the perfect algebaic properties, e.g. x^x=0, x^y=y^x, x^(~x)=0
        #x^k=y=> x^k^x=k=y^x
        mask, n=(1<<maximumBit)-1, len(nums)
        ans=[0]*n
        ans[-1]=nums[0]^mask
        for i in range(1, n):
            ans[~i]^=(ans[n-i]^nums[i])
        return ans
        
