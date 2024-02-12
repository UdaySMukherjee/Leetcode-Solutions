class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int], target: int) -> int:
            min_index = 0
            max_index = len(nums) - 1

            while min_index <= max_index:
                mid_index = min_index + (max_index - min_index) // 2
                mid_element = nums[mid_index]

                if mid_element == target:
                    return mid_index
                elif mid_element < target:
                    min_index = mid_index + 1
                else:
                    max_index = mid_index - 1

            return min_index

        return binary_search(nums, target)