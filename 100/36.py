class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    for k in range(9):
                        if ((board[i][k] == board[i][j] and k != j) or 
                            (board[k][j] == board[i][j] and k != i)):
                            return False
                    for k in range(3):
                        for l in range(3):
                            x = i / 3 * 3 + k
                            y = j / 3 * 3 + l
                            if x != i and y != j and board[x][y] == board[i][j]:
                                return False
        return True
