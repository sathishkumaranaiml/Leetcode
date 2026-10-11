class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=k=0
        n=len(chars)
        while(i<n):
            chars[k]=chars[i]
            k+=1
            j=i
            while j<n and chars[i]==chars[j]:
                j+=1
            le=j-i
            if le>1:
                for c in str(le):
                    chars[k]=c
                    k+=1
            i=j
        return k
                    