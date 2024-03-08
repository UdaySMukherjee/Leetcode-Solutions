class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_frequency = 0
        sum_frequency = 0
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            current_frequency = freq_dict[num]

            if current_frequency > max_frequency:
                max_frequency = current_frequency
                sum_frequency = current_frequency
            elif current_frequency == max_frequency:
                sum_frequency += current_frequency

        return sum_frequency  
