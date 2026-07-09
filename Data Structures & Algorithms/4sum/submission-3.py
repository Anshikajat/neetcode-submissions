class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=sorted(nums)
        i=0
        b=[]
        
        while(i<len(nums)):
            if(i>0 and a[i]==a[i-1]):
                i=i+1
                continue
            j=i+1    
            while(j<len(nums)):
                if(j>i+1 and a[j]==a[j-1]):
                  j=j+1
                  continue
                k=j+1
                l=len(a)-1  
                while(k<l):
                    if(a[i]+a[j]+a[k]+a[l]==target):
                        b.append([a[i],a[j],a[k],a[l]])
                    
                        l=l-1
                        k=k+1
                        while(k<l and a[k]==a[k-1]):
                            k=k+1
                    elif(a[i]+a[j]+a[k]+a[l]>target):
                        l=l-1
                    else:
                        k=k+1 
                j=j+1
            i=i+1
        return b                 



        