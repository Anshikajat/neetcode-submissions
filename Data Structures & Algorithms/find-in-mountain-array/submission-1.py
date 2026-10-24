class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        len=mountainArr.length()
        l=1
        r=len-2
        while(l<=r):
            m=(l+r)//2
            left=mountainArr.get(m-1)
            mid=mountainArr.get(m)
            right=mountainArr.get(m+1)
            if(left>mid>right):
                r=m-1
            elif(left<mid<right):
                l=m+1
            else:
                break
        preak=m 
        l=0
        r=preak
        while(l<=r):
            m=(l+r)//2
            val=mountainArr.get(m)
            if(val>target):
                r=m-1
            elif(val<target):
                l=m+1
            else:
                return m
        l=preak
        r=len-1
        while(l<=r):
            m=(l+r)//2
            val=mountainArr.get(m)
            if(val>target):
                l=m+1
            elif(val<target):
                r=m-1
            else:
                return m     
        return -1                                  