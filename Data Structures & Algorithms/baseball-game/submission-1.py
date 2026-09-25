class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        sum=0
        for i in operations:
            if(i.isdigit()):
                a.append(int(i))
            elif i.lstrip("-").isdigit():
                a.append(int(i))    
            elif(i=="+"):
                p=a[len(a)-1]+a[len(a)-2]
                a.append(p)
            elif(i=="D"):
                c=a[len(a)-1]*2
                a.append(c)
            else:
                a.pop()
        for j in a:
            sum+=j
        print(a)
        return sum                
