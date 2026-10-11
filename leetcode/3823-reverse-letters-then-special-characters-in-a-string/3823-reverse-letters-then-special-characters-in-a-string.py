class Solution:
    def reverseByType(self, s: str) -> str:
        sy=[]
        l=[]
        for i in s:
            if i.islower():
                l.append(i)
            else:
                sy.append(i)
       
        res=""
        i1=len(l)-1
        i2=len(sy)-1
        for i in range(len(s)):
            if s[i].islower():
                res+=l[i1]
                i1-=1
            else:
                res+=sy[i2]
                i2-=1
        return res


            





        