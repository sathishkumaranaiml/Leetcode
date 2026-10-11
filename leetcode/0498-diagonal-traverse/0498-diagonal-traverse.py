class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m=len(mat)
        n=len(mat[0])
        r=0
        c=0
        res=[]
        dirc=1
        for i in range(m*n):
            res.append(mat[r][c])
            if dirc==1:
                if  c==n-1:
                    r+=1
                    dirc=-1
                elif r==0:
                    c+=1
                    dirc=-1
                else:
                    r-=1
                    c+=1
            else:
                if r==m-1:
                    c+=1
                    dirc=1
                elif c==0:
                    r+=1
                    dirc=1
                else:
                    r+=1
                    c-=1
        return res

