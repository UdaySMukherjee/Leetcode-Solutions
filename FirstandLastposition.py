class Solution(object):
    def searchRange(self, nums, target):
        def binSearchleft(nums, min, max, target):
            while min < max:
                mid = (max + min) // 2
                if target > nums[mid]:
                    min = mid + 1
                elif target < nums[mid]:
                    max = mid
                else:
                    max = mid
            if min < len(nums) and nums[min] == target:
                return min
            else:
                return -1

        def binSearchright(nums, min, max, target):
            while min < max:
                mid = (max + min) // 2
                if target > nums[mid]:
                    min = mid + 1
                elif target < nums[mid]:
                    max = mid
                else:
                    min = mid + 1
            if max > 0 and nums[max - 1] == target:
                return max - 1
            else:
                return -1

        left = binSearchleft(nums, 0, len(nums), target)
        right = binSearchright(nums, 0, len(nums), target)
        return [left, right]
