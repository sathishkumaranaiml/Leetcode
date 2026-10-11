class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen=set()
        ans=set()
        current=s[:10]
        seen.add(current)
        if len(s)<10:
            return []
        for i in range(10,len(s)):
            current=current[1:]+s[i]
            if current in seen:
                ans.add(current)
            else:
                seen.add(current)
        return list(ans)
        