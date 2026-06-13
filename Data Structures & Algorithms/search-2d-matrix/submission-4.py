class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find the row using bs then run bs on that row

        # correct row is such that that last column first value which is greater is that row
        ROWS = len(matrix)
        COLS = len(matrix[ROWS-1])

        l = 0
        r = ROWS

        while l < r:
            m = (l + r) // 2

            if matrix[m][COLS-1] >= target: r = m
            else: l = m + 1
        
        # no such row found
        if l == ROWS: return False

        # bs on that row

        row = l
        l = 0
        r = COLS

        while l < r:
            m = (l + r) // 2
            if matrix[row][m] >= target: r = m
            else: l = m + 1
        
        if l == COLS: return False

        return matrix[row][l] == target 


