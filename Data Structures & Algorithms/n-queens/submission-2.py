class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # every queen before placing in the row - we check if its is attacked from above
        # diagonal or antigronal all from above
        # interesting fact - all diagonal sum is i +j and natigonal all celss obey i - j
        # when we reach teh last row that means all n queens were palced as we cant place if queen is attched ina row and we try to palce at every possible column in that row
        # if we cant place the queen in a column we backtarack and try the next row and so on
        board = [['.' for _ in range(n)] for _ in range(n)]        
        res = []
        cols = set()
        diagonals = set()
        antidiagonals = set()

        def backtrack(board,rows_cur):
            if rows_cur == n: 
                res.append(["".join(board[row]) for row in range(n)])
                return
            
            for col in range(n):
                diag = rows_cur + col
                anti_diag = rows_cur - col

            # try placing queen here if its not being attacked from above col, diag,anti
                if col in cols or diag in diagonals or anti_diag in antidiagonals:
                    continue
                # guanrantee its not being attacked and can be palced
                board[rows_cur][col] = 'Q'
                cols.add(col)
                diagonals.add(diag)
                antidiagonals.add(anti_diag)

                # explore the next row
                backtrack(board,rows_cur+1)

                # undo
                board[rows_cur][col] = '.'
                cols.remove(col)
                diagonals.remove(diag)
                antidiagonals.remove(anti_diag)
        backtrack(board,0)
        return res