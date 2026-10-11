class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        v={'a','e','i','o','u'}
        for i in s[:k]:
            if i in v:
                c+=1
        maxi=c
        for i in range(k,len(s)):
            if s[i-k] in v:
                c-=1
            if s[i] in v:
                c+=1
            maxi=max(maxi,c)
        return maxi

        