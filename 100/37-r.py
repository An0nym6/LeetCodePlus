# Don't overthink this. DFS is the easiest way

class Solution(object):
    def search(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    options = "123456789"
                    for k in range(9):
                        options = options.replace(board[i][k], "")
                        options = options.replace(board[k][j], "")
                    for k in range(3):
                        for l in range(3):
                            x = i / 3 * 3 + k
                            y = j / 3 * 3 + l
                            options = options.replace(board[x][y], "")
                    for option in options:
                        board[i][j] = option
                        if self.search(board):
                            return True
                    board[i][j] = "."
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        print self.search(board)
