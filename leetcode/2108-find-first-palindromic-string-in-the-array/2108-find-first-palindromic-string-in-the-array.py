class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def ispad(s):
            l=0
            r=len(s)-1
            while(l<=r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        for i in words:
            if ispad(i):
                return i
        return ""
    
            
        