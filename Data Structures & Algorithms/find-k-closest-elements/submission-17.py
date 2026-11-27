class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h=[]
        l=0
        for i in range(len(arr)):
            if(len(h)<k):
                h.append(arr[i])
            else:
                print(abs(x-arr[l])) 
                if(abs(x-h[0])>abs(x-arr[i])):
                    h.remove(h[0])
                    h.append(arr[i])
                    l+=1
        return h           

        