class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        se=set()
        l=0
        maxi=0
        for r in range(len(s)):
            while s[r] in se:
                se.discard(s[l])
                l+=1
            se.add(s[r])
            maxi=max(maxi,r-l+1)
        return maxi
    