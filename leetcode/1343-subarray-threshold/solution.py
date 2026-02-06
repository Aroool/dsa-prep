class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = sum(arr[:k])
        count = 0
        target_sum = k * threshold

        if curr_sum >= target_sum:
            count += 1
        
        for i in range(k, len(arr)):
            curr_sum = curr_sum + arr[i] - arr[i - k]

            if curr_sum >= target_sum:
                count +=1
        
        return count