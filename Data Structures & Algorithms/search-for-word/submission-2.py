class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # first the start could be from any char in the grid

        # then we do a backtracking serach from ervy position start
        # search on 4 cells to recurse later on and mark your current cell as visited
        # if none of them are at then return False

        rows = len(board)
        cols = len(board[0])
        moves = [(0,1),(1,0),(-1,0),(0,-1)]

        def find_word(i,j,match_at):
            if match_at >= len(word): return True
            if i >= rows or j >= cols: return False
            # mark current cell
            if board[i][j] == 1 or board[i][j] != word[match_at]:
                return False
            
            match_at += 1
            temp = board[i][j]
            board[i][j] = 1

            # explore 4 options in a loop
            for sh_i,sh_j in moves:
                new_i = i + sh_i
                new_j = j + sh_j
                if new_i < 0 or new_j < 0: continue
                if find_word(new_i,new_j,match_at):
                    # as soon as any match land fx returns True
                    return True

            # undo
            board[i][j] = temp

        for i in range(0,rows):
            for j in range(0,cols):
                if find_word(i,j,0):
                    return True
                
        # all match tried none retruned True
        return False
