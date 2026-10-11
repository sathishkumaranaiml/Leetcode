class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead
        condition
        org next state
        0     0     0
        1     0     1
        0     1     2
        1     1     3
        """
        def no_nei(r,c):
            nei=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if(i<0 or j<0 or i==m or j==n or(i==r and j==c)):
                        continue
                    elif board[i][j] in [1,3]:
                        nei+=1
            return nei
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                nei=no_nei(i,j)
                if board[i][j]==1:
                    if nei in [2,3]:
                        board[i][j]=3
                elif nei==3:
                    board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    board[i][j]=0
                elif board[i][j] in [2,3]:
                    board[i][j]=1
        
