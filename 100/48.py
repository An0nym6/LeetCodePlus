class Solution(object):
    def afterRotate(self, x, y):
        regionX = x / ((self.numRows + 1) / 2)
        regionY = y / ((self.numCols + 1) / 2)
        if (regionX, regionY) == (0, 0):
            return (y, self.numCols - x - 1)
        elif (regionX, regionY) == (0, 1):
            return (self.numRows - self.numCols + y, self.numCols - x - 1)
        elif (regionX, regionY) == (1, 0):
            return (self.numRows - self.numCols + y, self.numRows - x - 1)
        else:
            return (y, self.numRows - x - 1)

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        self.numRows = len(matrix)
        self.numCols = len(matrix[0])
        for x in range((self.numRows + 1) / 2):
            for y in range(self.numCols / 2):
                x_, y_ = self.afterRotate(x, y)
                temp = matrix[x_][y_]
                matrix[x_][y_] = matrix[x][y]
                x__, y__ = self.afterRotate(x_, y_)
                temp_ = matrix[x__][y__]
                matrix[x__][y__] = temp
                x___, y___ = self.afterRotate(x__, y__)
                temp__ = matrix[x___][y___]
                matrix[x___][y___] = temp_
                matrix[x][y] = temp__
                print (x, y), (x_, y_), (x__, y__), (x___, y___)
        