class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        lps=[0]*n
        i=1
        l=0
        while(i<n):
            if s[i]==s[l]:
                l+=1
                lps[i]=l
                i+=1
            else:
                if (l>0):
                    l=lps[l-1]
                else:
                    lps[i]=0
                    i+=1
        pt=n-lps[n-1]
        return  lps[n-1]>0 and n%pt==0