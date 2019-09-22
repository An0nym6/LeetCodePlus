class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        visited = []
        for i in range(m):
            visited.append([0] * n)
        ans = []
        row = 0
        col = 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        currentDirIndex = 0
        while len(ans) < m * n:
            ans.append(matrix[row][col])
            visited[row][col] = 1
            currentDir = direction[currentDirIndex % 4]
            if (not(row + currentDir[0] >= 0 and row + currentDir[0] < m and
                    col + currentDir[1] >= 0 and col + currentDir[1] < n and
                    visited[row + currentDir[0]][col + currentDir[1]] == 0)):
                currentDirIndex += 1
                currentDir = direction[currentDirIndex % 4]
            row += currentDir[0]
            col += currentDir[1]
        return ans
