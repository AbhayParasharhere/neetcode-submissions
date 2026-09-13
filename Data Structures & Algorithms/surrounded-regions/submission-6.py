class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # run dfs from the outermost row and column cells which are O 
        # basically the vulnerable cells mark them as V to ensure we dont touch them
        # second pass mark every O cell cellto X
        # third pass revrt those V cells to O
        m = len(board[0])
        n = len(board)

        visited = [[False for _ in range(m)] for _ in range(n)]
        direc = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c,fill):
            stack = []
            stack.append((r,c))
            board[r][c] = fill
            while stack:
                ui,uj = stack.pop()
                for delta_i,delta_j in direc:
                    vi = ui + delta_i
                    vj = uj + delta_j
                    if vi < 0 or vj < 0 or vi >= n or vj >= m or board[vi][vj] != 'O':
                        continue
                    board[vi][vj] = fill
                    stack.append((vi,vj))

        # first row and last row
        for col in range(m):
            if board[0][col] == "O":
                # fill with N
                dfs(0,col,'N')
            if board[n-1][col] == "O":
                dfs(n-1,col,'N')
        
        # first col and last col
        for row in range(n):
            if board[row][0] == "O":
                dfs(row,0,'N')
            if board[row][m-1] == "O":
                dfs(row,m-1,'N')
        
        # now simpply fill all Os to X as they are not neighbour of boudnaries O's
        for i in range(0,n):
            for j in range(0,m):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # now revret all N to O
        for i in range(0,n):
            for j in range(0,m):
                if board[i][j] == "N":
                    board[i][j] = "O"
        
