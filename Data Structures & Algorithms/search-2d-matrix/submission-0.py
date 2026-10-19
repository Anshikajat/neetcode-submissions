class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            a=len(matrix[i])-1
            if(matrix[i][a]>=target):
                s=0
                l=a
                while(s<=l):
                    m=(s+l)//2
                    if(matrix[i][m]==target):
                        return True
                    elif(matrix[i][m]<target):
                        s=m+1
                    else:
                        l=m-1
            else:
                continue
        return False                    
                    
        