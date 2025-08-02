import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1

        heap = []
        for num, freq in frequency_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]