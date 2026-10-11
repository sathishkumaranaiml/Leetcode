class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=list(word)
        l=0

        for i in range(len(s)):
            if(s[i]==ch):
                r=i
                while(l<r):
                    s[l],s[r]=s[r],s[l]
                    l+=1
                    r-=1
                break
        return "".join(s)

        