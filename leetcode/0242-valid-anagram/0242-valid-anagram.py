class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h=[0]*26
        n1,n2=len(s),len(t)
        if n1!=n2:
            return False
        for i in range(n1):
            h[ord(s[i])-ord('a')]+=1
            h[ord(t[i])-ord('a')]-=1
        for i in range(26):
            if h[i]!=0:
                return False
        return True