class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merege(nums,h,m,l):
            i=h
            j=m+1
            tem=[]
            while(i<=m and j<=l):
                if(nums[i]>nums[j]):
                    tem.append(nums[j])
                    j=j+1
                else: 
                     tem.append(nums[i])
                     i=i+1
            while(i<=m):
                
                tem.append(nums[i])
                i=i+1     
            while(j<=l):
                
                tem.append(nums[j])
                j=j+1          
            for i in range(0,len(tem)):
                nums[i+h]=tem[i]        


        
        def mereges(nums,h,l):
            if(h<l):
                    
                m=(h+l)//2     
                mereges(nums,h,m)
                mereges(nums,m+1,l)
                merege(nums,h,m,l)

        mereges(nums,0,len(nums)-1)
        return nums
            

        
        