class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # Create the 2d sum array
        self.arr = [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                top = 0
                left = 0
                intersect = 0
                if i - 1 >= 0:
                    top = self.arr[i - 1][j]
                if j - 1 >= 0:
                    left = self.arr[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    intersect = self.arr[i-1][j-1]
                self.arr[i][j] += top + left - intersect

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        intersect = 0
        top_rt = 0
        bottom_lt = 0
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            intersect = self.arr[row1 - 1][col1 - 1]
        if row1 - 1 >= 0:
            top_rt = self.arr[row1-1][col2]
        if col1 - 1 >= 0:
            bottom_lt = self.arr[row2][col1 - 1]
        return self.arr[row2][col2] + intersect - top_rt - bottom_lt
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
