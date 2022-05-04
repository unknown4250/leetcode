class Solution(object):
    def isValidSudoku(self, board):
        dict_row = {}
        dict_column = {}
        dict_grid = {}

        for i in range(9):
            for j in range(9):
                # row
                if board[i][j] != ".": 
                    if board[i][j] not in dict_row:
                        dict_row[board[i][j]] = 1
                    else:
                        return False
                # column
                if board[j][i] != ".": 
                    if board[j][i] not in dict_column:
                        dict_column[board[j][i]] = 1
                    else:
                        return False
                # box
                if i % 3 == 0 and j % 3 == 0:
                    dict_grid.clear()
                    for w in range(3):
                        for h in range(3):
                            if i + w < 9 and j + h < 9 and board[i+w][j+h] != ".":
                                print(board[i+w][j+h])
                                if board[i+w][j+h] not in dict_grid:
                                    dict_grid[board[i+w][j+h]] = 1
                                else:
                                    return False

            dict_row.clear()
            dict_column.clear()

        return True