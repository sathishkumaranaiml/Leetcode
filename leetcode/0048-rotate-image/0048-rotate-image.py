class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        sr,er=0,n-1
        sc,ec=0,n-1
        while(sr<er):
            for i in range(sr,ec+1):
                matrix[sr][i],matrix[i][sr]=matrix[i][sr],matrix[sr][i]
            sr+=1
        for i in range(n):
            l=0
            r=n-1
            while(l<r):
                matrix[i][r],matrix[i][l]=matrix[i][l],matrix[i][r]
                l+=1
                r-=1
        return matrix

             


            
        