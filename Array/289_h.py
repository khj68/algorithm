class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        
        r = len(board)
        c = len(board[0])
        
        for y in range(r):
            for x in range(c):
                count = 0
                for k in range(8):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    
                    if ny < 0 or nx < 0 or ny == r or nx == c:
                        continue
                    
                    if board[ny][nx] > 0:
                        count += 1
                
                if board[y][x] == 1:
                    if count not in (2, 3):
                        board[y][x] = 2
                else:
                    if count == 3:
                        board[y][x] = -1
        
        for y in range(r):
            for x in range(c):
                if board[y][x] == 2:
                    board[y][x] = 0
                elif board[y][x] == -1:
                    board[y][x] = 1
        
                    
                