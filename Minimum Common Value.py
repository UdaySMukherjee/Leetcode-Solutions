class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        i,j = 0,0
        while(i<n1 and j<n2):
            if nums1[i] > nums2[j]:
                j+=1
            elif nums2[j] > nums1[i]:
                i+=1
            else:
                return nums1[i]
        return -1
            
