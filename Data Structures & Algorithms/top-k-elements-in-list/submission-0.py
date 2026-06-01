class Solution(object):
    def topKFrequent(self, nums, k):

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [sorted_freq[i][0] for i in range(k)]