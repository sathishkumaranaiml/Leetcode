class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)!=len(t):
            return False
        m={}
        m1={}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=i
            if t[i] not in m1:
                m1[t[i]]=i
            if m1[t[i]]!=m[s[i]]:
                return False
        return True



            