class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sortme(arr,l,h):
            if(l<h):
                m=(l+h)//2
                sortme(arr,l,m)
                sortme(arr,m+1,h)
                merges(arr,l,m,h)
        def merges(arr,l,m,h):
            i=l
            j=m+1
            p=[]
            while(i<=m and j<=h):
                if(arr[i]<arr[j]):
                    p.append(arr[i])
                    i+=1
                else:
                    p.append(arr[j])
                    j+=1
            while(i<=m):
                p.append(arr[i])
                i+=1 
            while(j<=h):
                p.append(arr[j])
                j+=1
            for k in range(len(p)):
                arr[l+k]=p[k]      
        sortme(nums,0,len(nums)-1)
        return nums                     

    

        