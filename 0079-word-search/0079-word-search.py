class Solution(object):
    def exist(self, board, word):

        def backtracking(x, y, candidate):
            # word 끝까지 탐색 완료했으면 존재하는 단어가 있다는 의미, True 리턴
            if len(candidate) == 0:
                return True

            # board 범위 벗어난 경우 False 리턴
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False

            # 현재 위치의 문자와 단어의 문자가 같은 경우
            if board[x][y] == candidate[0]:
                # 현재 위치를 재탐색하지 않기 위해 값 변경
                board[x][y] = '-'

                # 상하좌우 탐색
                if backtracking(x+1, y, candidate[1:]) or backtracking(x-1, y, candidate[1:]) or \
                    backtracking(x, y+1, candidate[1:]) or backtracking(x, y-1, candidate[1:]):
                        return True

                # 백트래킹을 위해 원래 값으로 변경
                board[x][y] = candidate[0]

            return False
            
        # board의 전체 값 탐색
        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtracking(i, j, word):
                    return True
        return False           

        
        