class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p=[]
        for i in range(len(position)):
            p.append((position[i],speed[i]))
        p.sort(reverse=True)
        st=[]
        for p,s in p:
            st.append((target-p)/s)
            if(len(st)>=2 and st[-1]<=st[-2]):
                st.pop()
        return len(st)           