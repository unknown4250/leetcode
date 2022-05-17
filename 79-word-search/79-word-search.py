class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, word, visited, row, col):
                    return True
        return False
    
    # check whether can find word, start at (i,j) position
    def dfs(self, board, word, visited, i, j):
        # all characters are checked
        if not word: 
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
            visited[i][j] or word[0] != board[i][j]:
            return False
        
        visited[i][j] = True

        if self.dfs(board, word[1:], visited, i-1, j) or \
                self.dfs(board, word[1:], visited, i+1, j) or \
                self.dfs(board, word[1:], visited, i, j-1) or \
                self.dfs(board, word[1:], visited, i, j+1):
                return True
        
        # there is no solution in the path so reset the candidacy of that position
        visited[i][j] = False

        return False