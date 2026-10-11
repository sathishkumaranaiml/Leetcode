class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=set()
        res=0
        for i in s:
            if i in m:
                m.remove(i)
                res+=2
            else:
                m.add(i)
        if m:
            return res+1
        else:
            return res        

