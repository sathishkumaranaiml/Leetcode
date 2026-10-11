class Solution:
    def equalSubstring(self, s: str, t: str,k: int) -> int:
        n=len(s)
        res=l=sw=0
        for i in range(n):
            sw+=abs(ord(s[i])-ord(t[i]))
            while sw>k:
                sw-=abs(ord(s[l])-ord(t[l]))
                l+=1
            res=max(res,i-l+1)
        return res

        
        
