class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first we find the correct row using binary search
        # then we find the correct column
        # find row
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows

        # first col check - 
        # the boundary or first T such that its greater or equal than target
        while l < r:
            m = (l+r) //2
            if matrix[m][0] > target: r = m
            else: l = m + 1
        if l == 0: return False
        row_f = l - 1

        #  now interested in the element in this row
        #  use pattern 1 here
        l = 0
        r = cols

        while l < r:
            m = (l+r) //2
            if matrix[row_f][m] >= target: r = m
            else: l = m + 1
        return l < cols and matrix[row_f][l] == target

