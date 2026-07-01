class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        ROW = len(matrix)
        COL = len(matrix[0])
        
        n = ROW*COL
        r = n
        row,col = 0, 0
        while l < r:
            m = (l+r) // 2
            row = m // COL
            col = m % COL
            # say 5th cell - is row 1 and col 0 
            # 5 / 3 - is 1, 5 / 4 = 1
            if  matrix[row][col]>= target: r = m
            else: l = m + 1
        
        if l == n: return False
        return target == matrix[l//COL][l%COL]