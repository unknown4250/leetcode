class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            arr_row = []
            arr_column = []
            for j in range(9):
                # row
                if board[i][j] != "." and board[i][j] in arr_row:
                        return False
                else:
                        arr_row.append(board[i][j])
                # column
                if board[j][i] != "." and board[j][i] in arr_column:
                        return False
                else:
                        arr_column.append(board[j][i])


        # grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                arr_grid = []
                for w in range(3):
                    for h in range(3):
                        if board[i+w][j+h] != "." and board[i+w][j+h]in arr_grid:
                            return False
                        else:
                            arr_grid.append(board[i+w][j+h])
        return True
