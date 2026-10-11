class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c=0
        m={}
        l=0
        for i in range(len(s)):
            m[s[i]]=m.get(s[i],0)+1
            while len(m)==3:
                c+=len(s)-i
                m[s[l]]-=1
                if m[s[l]]==0:
                    del m[s[l]]
                l+=1
        return c
                