class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2 ways to do this 2 separate bs to find teh correct row then the ht
        # or teh otehr way to convert evrything into a single listand bs then
        ROWS = len(matrix)
        COLS = len(matrix[0])
        n = ROWS * COLS
        l = 0
        r = n
        # all cells between 0 and r - 1 so r is correct off by 1

        # 0 1 2  3 - row 0
        # 4 5 6  7 - row 1
        # 8 9 10 11 - row 2
        while l < r:
            m = (l + r) // 2
            # say 10th cell has row 2 and col 2 - we have total 3 rows and 4 cols 
            #  then row is 10 / 3 around 2 in row, and 10 % 4 = 2
            # now for cell 5th - 5/4 is 1 which is corr and 5%4 1 corr
            row = m // COLS
            col = m % COLS
            elem = matrix[row][col]
            if elem >= target: r = m
            else: l = m + 1
        if l//COLS >= ROWS or l%COLS >= COLS:
            return False
        found = matrix[l//COLS][l%COLS]
        if found == target: 
            return True
        else:
            return False
