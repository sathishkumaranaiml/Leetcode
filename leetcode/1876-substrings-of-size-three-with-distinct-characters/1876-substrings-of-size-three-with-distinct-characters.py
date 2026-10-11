class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        """
        c=0
        for i in range(len(s)-2):
            if len(set(s[i:i+3]))==3:
                c+=1
        return c

        