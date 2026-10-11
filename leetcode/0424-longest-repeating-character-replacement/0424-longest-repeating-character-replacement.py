class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        m={}
        maxi=0
        l=0
        for i in range(len(s)):
            m[s[i]]=m.get(s[i],0)+1
            maxi=max(maxi,m[s[i]])
            if i-l+1-maxi>k:
                m[s[l]]-=1
                l+=1
        return len(s)-l
        