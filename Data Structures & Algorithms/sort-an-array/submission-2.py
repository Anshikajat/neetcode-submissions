class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    

        def merge(nums, i, m, j):
            a = []

            p = m          # end of left half
            q = i          # starting index for copying back
            m = m + 1      # start of right half

            while i <= p and m <= j:
                if nums[i] > nums[m]:
                    a.append(nums[m])
                    m += 1
                else:
                    a.append(nums[i])
                    i += 1

            while i <= p:
                a.append(nums[i])
                i += 1

            while m <= j:
                a.append(nums[m])
                m += 1

            nums[q:j+1] = a     # copy back

        def divmerge(nums, i, j):
            if i >= j:
                return

            m = (i + j) // 2

            divmerge(nums, i, m)
            divmerge(nums, m + 1, j)

            merge(nums, i, m, j)

        divmerge(nums, 0, len(nums) - 1)
        return nums