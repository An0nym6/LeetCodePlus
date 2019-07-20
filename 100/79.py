class Solution(object):
    def search(self, x, y, counter):
        if counter == len(self.word):
            return True
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (i >= 0 and j >= 0 and i < self.height and j < self.width and
                not (i, j) in self.visited and
                self.board[i][j] == self.word[counter]):
                self.visited.add((i, j))
                if self.search(i, j, counter + 1):
                    return True
                self.visited.remove((i, j))
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        self.word = word
        for i in range(self.height):
            for j in range(self.width):
                if word[0] == board[i][j]:
                    self.visited = set([(i, j)])
                    if self.search(i, j, 1):
                        return True
        return False
