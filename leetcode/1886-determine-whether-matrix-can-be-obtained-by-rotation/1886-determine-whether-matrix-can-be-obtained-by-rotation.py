class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for i in range(4):
            if mat== target:
                return True
            for  i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in mat:
                i.reverse()
        return False