class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=sorted(nums)
        i=0
    
        
        b=[]
        while(i<len(a)):
            if(i>0 and a[i]==a[i-1]):
                i+=1
                continue
            j=i+1
            k=len(a)-1
            while(j<k):
                if(a[i]+a[j]+a[k]==0):
                    b.append([a[i],a[j],a[k]])
                    j=j+1
                    k=k-1
                    while(j<k and a[j]==a[j-1]):
                        j=j+1
                elif(a[i]+a[j]+a[k]>0):
                    k=k-1
                else:
                    j=j+1
            i=i+1        
        return b                



        
        