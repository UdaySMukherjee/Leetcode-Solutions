class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        # First pass: Push indices of potential left boundaries into the stack
        # We only push indices where the value is smaller than the previous stack top
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        ans = 0

        # Second pass: Iterate from right to left to find the maximum width ramp
        for i in range(n - 1, 0, -1):
            # While the stack is not empty and the current element is greater than or equal to the stack top
            while stack and nums[stack[-1]] <= nums[i]:
                # Calculate the width of the ramp and update the maximum
                ans = max(ans, i - stack[-1])
                # Remove the top element as we've found a valid ramp for it
                stack.pop()

        # Return the maximum width ramp found
        return ans
