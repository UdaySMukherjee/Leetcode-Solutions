class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # using prefix sum to track the number of subarrays with an odd sum
        # pf_sum[0] record the number of prefix sum with an even sum
        # pf_sum[1] record the number of prefix sum with an odd sum
        pf_sum = [1, 0]
        
        rs, ans = 0, 0
        for n in arr:
            rs += n
            if rs % 2:
                ans += pf_sum[0]
                pf_sum[1] += 1
            else:
                ans += pf_sum[1]
                pf_sum[0] += 1
        return ans % 1000000007
        
