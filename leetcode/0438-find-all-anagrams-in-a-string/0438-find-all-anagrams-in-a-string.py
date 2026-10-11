class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        h=[0]*26
        h1=[0]*26
        res=[]
        if len(p)>len(s):
            return []
        for i in range(len(p)):
            h[ord(p[i])-ord('a')]+=1
            h1[ord(s[i])-ord('a')]+=1
        if h1==h:
            res.append(0)
        for i in range(len(p),len(s)):
            h1[ord(s[i])-ord('a')]+=1
            h1[ord(s[i-len(p)])-ord('a')]-=1
            if h1==h:
                res.append(i-len(p)+1)
        return res