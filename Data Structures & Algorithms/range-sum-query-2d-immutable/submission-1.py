class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r=len(matrix)
        c=len(matrix[0])
        self.sum=[[0]*(c+1) for i in range(r+1)]
        for i in range(r):
            pre=0
            for j in range(c):
                pre+=matrix[i][j]
                ab=self.sum[i][j+1]
                self.sum[i+1][j+1]=pre+ab        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1=row1+1
        r2=row2+1
        c1=col1+1
        c2=col2+1
        return(self.sum[r2][c2]-self.sum[r1-1][c2]-self.sum[r2][c1-1]+self.sum[r1-1][c1-1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)