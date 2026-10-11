class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m={}
        res=0
        l=0
        for i in range(len(s)):
            m[s[i]]=m.get(s[i],0)+1
            while m[s[i]]>2:
                m[s[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res

        