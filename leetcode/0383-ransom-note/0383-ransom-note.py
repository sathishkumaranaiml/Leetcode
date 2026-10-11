class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m=Counter(magazine)
        
        for i in ransomNote:
            m[i]-=1
            if  m[i]<0:
                return False
        return True
        