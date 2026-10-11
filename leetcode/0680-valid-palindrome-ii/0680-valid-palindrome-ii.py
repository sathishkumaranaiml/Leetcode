class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(i,j):
            while(i<j):
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]==s[j]:
                j-=1
                i+=1
            else:
                return ispal(i+1,j) or ispal(i,j-1)
        return True
            
                

                
       
            

        
        