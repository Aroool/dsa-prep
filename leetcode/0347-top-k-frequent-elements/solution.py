from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        n = len(nums)
        bucket = [[] for i in range(n+1)]
        for num, f in freq.items():
            bucket[f].append(num)
        result = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    