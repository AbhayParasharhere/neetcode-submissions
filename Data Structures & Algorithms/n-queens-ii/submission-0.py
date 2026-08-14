class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        diagonals = set()
        antidiagonals = set()
        res = 0
        def backtrack(cur_row):
            nonlocal res
            if cur_row == n:
                # every config is unqiue when we hit this condition
                res += 1
                return
            
            for col in range(n):
                diag = cur_row + col
                anti_diag = cur_row - col
                if col in columns or diag in diagonals or anti_diag in antidiagonals:
                    continue
                
                # we can palce the queen here commit to it
                columns.add(col)
                diagonals.add(diag)
                antidiagonals.add(anti_diag)
                backtrack(cur_row+1)
                # undo
                columns.remove(col)
                diagonals.remove(diag)
                antidiagonals.remove(anti_diag)
        backtrack(0)
        return res


            
