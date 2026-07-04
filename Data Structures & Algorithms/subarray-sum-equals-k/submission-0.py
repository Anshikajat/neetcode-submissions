class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix = 0
        h = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in h:
                count += h[prefix - k]

            h[prefix] = h.get(prefix, 0) + 1
                
        return count             


        