class Solution:
    def balancedString(self, s: str) -> int:
        count={"Q":0,"W":0,"E":0,"R":0}
        for i in s:
            count[i]+=1
        l=0
        n=len(s)
        need=n//4
        ans=n
        c=0
        for i in range(n):
            if count[s[i]]==need:
                c+=1
        if n==c:
            return 0
        for r in range(n):
            count[s[r]]-=1
            while l<=r and all(count[i]<=need for i in "QWER" ):
                ans=min(ans,r-l+1)
                count[s[l]]+=1
                l+=1
        return ans