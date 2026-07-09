class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(i,j):
            while(i<j):
                p=nums[i]
                nums[i]=nums[j]
                nums[j]=p
                i+=1
                j-=1
        k = k % len(nums)        
        n=len(nums)
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
                 
        



        