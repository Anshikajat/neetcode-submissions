class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        a = []

        # Find possible candidates
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

            if len(h) == 3:
                d = {}
                for n, k in h.items():
                    if k > 1:
                        d[n] = k - 1
                h = d

        # Count candidates again
        count = {}

        for i in nums:
            if i in h:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1

        # Check which candidates occur more than n/3 times
        for i, j in count.items():
            if j > len(nums) / 3:
                a.append(i)

        return a