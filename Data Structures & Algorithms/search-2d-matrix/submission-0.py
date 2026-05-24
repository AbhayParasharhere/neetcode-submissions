class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # First find the correct l and r bounds
        #  such that elem[l] <= target and elem[r] > target

        # find the correct row
        l, r = 0, rows

        while l < r:
            m = (l+r) //2
            if matrix[m][cols-1] >= target: r = m
            else: l = m + 1
        if l == rows: return False # out of bound

        # l contains the correct row for our target
        row_f = l

        # Now we need to find the correct cell within this row
        l = 0
        r = cols

        while l < r:
            m = (l+r) // 2
            if matrix[row_f][m] > target: r = m
            else: l = m + 1
        # Now case of where last F has target, so l - 1 is the correct col

        if l == 0: return False
        return matrix[row_f][l-1] == target

