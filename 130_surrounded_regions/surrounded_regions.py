class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/surrounded-regions/
    """
    directions = [-1, 0, 1, 0, -1]
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        从所有边界上的O开始深度优先遍历，找到所有与之相连的O，并修改为M
        遍历完成后，所有剩下的O都是被X包围的，最后将O修改为X，M还原为O
        """
        height = len(board)
        width = len(board[0])
        if height == 1 or width == 1:
            return

        for i in range(height):
            for j in range(width):
                if (i == 0 or i == height - 1 or j == 0 or j == width - 1) and board[i][j] == "O":
                    self.dfs(board, i, j)
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == "M":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, board, r, c):
        if board[r][c] != "O":
            return
        board[r][c] = "M"
        for i in range(4):
            x = r + Solution.directions[i]
            y = c + Solution.directions[i + 1]
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):
                self.dfs(board, x, y)
        

if __name__ == "__main__":
    s = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print("raw board:")
    for row in board:
        print(row)
    s.solve(board)
    print("\nnew board:")
    for row in board:
        print(row)
