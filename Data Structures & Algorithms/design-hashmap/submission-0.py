class MyHashMap:

    def __init__(self):
        self.p=[]
        for i in range(0,1000):
            self.p.append([])

        

    def put(self, key: int, value: int) -> None:
        b=key%1000
        if(self.p[b]==[]):
            self.p[b].append(key)
            self.p[b].append(value)
        else:
            self.p[b][1]=value    

        

    def get(self, key: int) -> int:
        b=key%1000
        if(self.p[b]):
           return self.p[b][1]
        else:
            return -1   
        

    def remove(self, key: int) -> None:
        b=key%1000
        self.p[b].clear()
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)