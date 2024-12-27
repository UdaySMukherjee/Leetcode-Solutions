class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Initialize variables
        max_score = 0
        max_i_value = values[0] + 0  # This is values[i] + i for the first element

        # Iterate through the array starting from the second element
        for j in range(1, len(values)):
            # Calculate the score for the current pair (i, j)
            max_score = max(max_score, max_i_value + values[j] - j)

            # Update max_i_value to include the current index
            max_i_value = max(max_i_value, values[j] + j)

        return max_score
