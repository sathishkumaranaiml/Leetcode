class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        l=0
        cus=0
        for r in range(n+abs(k)):
            cus+=code[r%n]
            if r-l+1>abs(k):
                cus-=code[l%n]
                l=(l+1)%n
            if r-l+1==abs(k):
                if k>0:
                    res[(l-1)%n]=cus
                elif k<0:
                    res[(r+1)%n]=cus
        return res


             