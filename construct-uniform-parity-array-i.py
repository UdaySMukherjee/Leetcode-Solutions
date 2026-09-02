class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_cnt = sum(1 for num in nums1 if num & 1)

        # try transforming to odd
        can_transform = True
        for num in nums1:
            if (num % 2 == 0) and (odd_cnt == 0):
                can_transform = False
                break

        if can_transform:
            return True

        # try transforming to even
        for num in nums1:
            if (num & 1) and (odd_cnt < 2):
                return False

        return True
