class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=len(nums2)-1
        t=n+m-1
        
        while(j>=0):
            if(i>=0 and nums1[i]>nums2[j]):
                nums1[t]=nums1[i]
                i-=1
                t-=1
            else:
                
                nums1[t]=nums2[j]
                j-=1
                t-=1  
                   
        