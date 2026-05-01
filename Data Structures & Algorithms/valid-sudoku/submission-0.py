from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # using default dictionary which is a dictory where each value is a set
        # we map each of the square value  to one of these 9 keys 0,0 - 1st square or 0,1 2nd square
        # this is done using i//3 and j //3 so each box is mapped to one of those 9 squares
        #     (0,0): {"5", "3", "7"},  # top-left box
        # (0,1): {"1", "9"},       # top-middle box
        # (1,0): {"4"},            # middle-left box
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        # These are hashmap where each value is a set

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[f"{i // 3},{j // 3}"]
                ):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[f"{i // 3},{j // 3}"].add(board[i][j])
        return True

