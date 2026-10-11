class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        i=0
        while(i<n-1):
            if s[i]!=s[n-1]:
                return 2
            i+=1
            n-=1
        return  1 