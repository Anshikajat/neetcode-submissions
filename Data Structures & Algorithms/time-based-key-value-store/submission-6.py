class TimeMap:

    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(timestamp not in self.d):
            self.d[timestamp]={}
        self.d[timestamp][key]=value    

    def get(self, key: str, timestamp: int) -> str:
        if(timestamp in self.d):
            if(key in self.d[timestamp]):
                return self.d[timestamp][key]
            
            
        a=-1    
        for i in self.d:
            if(i>a and i<=timestamp and key in self.d[i]):
                a=i
            
            
        if(a!=-1):
            if(key in self.d[a]):
                return self.d[a][key]        
        return ""    
