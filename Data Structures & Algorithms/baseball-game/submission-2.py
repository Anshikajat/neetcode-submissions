class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        su=0
        for i in operations:
            if(i=="+"):
                a=s[-1]
                b=s[-2]
                s.append(a+b)
            elif(i=="D"):
                s.append(2*s[-1])
            elif(i=="C"):
                s.pop()
            else:
                s.append(int(i))
        for j in s:
            su+=j
        return su                       

        