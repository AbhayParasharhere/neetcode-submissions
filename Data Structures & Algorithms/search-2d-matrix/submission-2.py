class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # using a single pass bs 
        rows = len(matrix)
        cols = len(matrix[0])

        l,r = 0, rows*cols 
        while l < r:
            m = (l + r ) //2
            R = m // cols
            C = m % cols
            print(R,C)
            if matrix[R][C] >= target: r = m
            else: l = m + 1
        
        if l == rows * cols: return False
        R = l // cols
        C = l % cols
        return matrix[R][C] == target

