class Solution:
    def search(self, nums: List[int], target: int) -> int:
            res=-1
            l=0
            r=len(nums)-1
            while(l<=r):
                m=(l+r)//2
                print(m)
                if(nums[m]==target):
                        return m
                if(nums[l]<nums[r]):
                    print("a")
                    if(nums[m]>target):
                        r=m-1
                    else:
                        l=m+1
                else:
                    if(nums[l]<=nums[m]):
                        print("b")
                        if(target>=nums[l] and  target <nums[m]):
                        
                            r=m-1
                        else:
                        
                            l=m+1
                    else:
                        print("c")
                        if(target>=nums[l] or target <nums[m]):
                            print("ca")
                            r=m-1
                        else:
                            print("cb")
                            l=m+1        
            return res                   
                                        
    