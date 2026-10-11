class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        m={}
        for i in s:
            m[i]=m.get(i,0)+1
        if len(s)<k:
            return 0
        res=0
        for i in s:
            if m[i]<k:
                parts=s.split(i)
                for part in parts:
                    res=max(self.longestSubstring(part,k),res)
                return res
        return len(s)


            
        