class Solution(object):
    def nextMove(self, startRow, queensLeft):
        # End condition
        if queensLeft == 0:
            temp = []
            for row in self.board:
                str = ""
                temp.append(str.join(row))
            self.ans.append(temp)
        # Pruned
        if self.n - startRow < queensLeft:
            return
        for row in range(startRow, self.n):
            for col in range(0, self.n):
                if (self.rowCheck[row] == 0 and self.colCheck[col] == 0 and
                    self.downSlope[row - col] == 0 and
                    self.upSlope[row + col] == 0):
                    self.board[row][col] = 'Q'
                    self.rowCheck[row] = 1
                    self.colCheck[col] = 1
                    self.downSlope[row - col] = 1
                    self.upSlope[row + col] = 1
                    self.nextMove(row + 1, queensLeft - 1)
                    self.board[row][col] = '.'
                    self.rowCheck[row] = 0
                    self.colCheck[col] = 0
                    self.downSlope[row - col] = 0
                    self.upSlope[row + col] = 0

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = []
        self.board = []
        self.n = n
        self.rowCheck = [0] * n
        self.colCheck = [0] * n
        self.downSlope = [0] * (2 * n)
        self.upSlope = [0] * (2 * n)
        for i in range(n):
            self.board.append(['.'] * n)
        self.nextMove(0, n)
        return self.ans
