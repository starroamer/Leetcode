from typing import List

class Solution:
    direction_col = [1, 0]
    direction_row = [0, 1]
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        self.row = len(obstacleGrid)
        if self.row == 0:
            return []
        self.col = len(obstacleGrid[0])
        if self.col == 0:
            return []
        visit = [[0 for i in range(self.col)] for i in range(self.row)]
        
        path = self.findPath(obstacleGrid, 0, 0, visit)
        return path
    
    def findPath(self, obstacleGrid, row, col, visit):
        # 超出边界
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            return []
        # 遇到障碍
        if obstacleGrid[row][col] == 1:
            return []
        # 之前路径已经经过该节点
        if visit[row][col] == 1:
            return []

        visit[row][col] = 1

        # 到达终点
        if row == self.row - 1 and col == self.col - 1:
            return [[row, col]]

        for i in range(2):
            row_move = Solution.direction_row[i]
            col_move = Solution.direction_col[i]
            new_row = row + row_move
            new_col = col + col_move
            path = self.findPath(obstacleGrid, new_row, new_col,visit)
            if path:
                path = [[row, col]] + path
                return path

        # 如果上下左右都能走，回溯时就需要将visit矩阵中当前节点的状态恢复
        # visit[row][col] = 0

        return []
        
        
if __name__   == "__main__":
    s = Solution()
    grid = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]]
    path = s.pathWithObstacles(grid)
    print(path)
