class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        
        h1=[0]*26
        h2=[0]*26
        for i in range(len(s1)):
            h1[ord(s1[i])-ord('a')]+=1
            h2[ord(s2[i])-ord('a')]+=1
        if h1==h2:
            return True
        for i in range(len(s1),len(s2)):
            h2[ord(s2[i])-ord('a')]+=1
            h2[ord(s2[i-len(s1)])-ord('a')]-=1
            if h1==h2:
                return True
        return False




        