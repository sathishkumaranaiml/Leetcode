class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for _ in range(n)]
        c=1
        
        
        l,r=0,n-1
        t,b=0,n-1
        res=[]
        while(l<=r and t<=b):
            for i in range(l,r+1):
                matrix[t][i]=c
                c+=1
            t+=1
            for i in range(t,b+1):
                matrix[i][r]=c
                c+=1
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    matrix[b][i]=c
                    c+=1
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    matrix[i][l]=c
                    c+=1
                l+=1
        return matrix
               
        
