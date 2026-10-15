class FreqStack:

    def __init__(self):
        self.h={}
        self.h1={}

    def push(self, val: int) -> None:
        if(val not in self.h):
            self.h[val]=1
        else:
            self.h[val]+=1
        if(self.h[val] in self.h1):
            self.h1[self.h[val]].append(val)
        else:
            self.h1[self.h[val]]=[val]            

        

    def pop(self) -> int:
        
        key = max(self.h1.keys())
        p=self.h1[key].pop()
        if(not self.h1[key]):
            del self.h1[key]
        self.h[p]-=1
        return p



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()