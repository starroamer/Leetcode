class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/max-area-of-island/description/
    """
    directions = [-1, 0, 1, 0, -1]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        max_area = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))

        return max_area
    
    def dfs(self, grid, r, c):
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        area = 1
        for i in range(4):
            x = r + Solution.directions[i]
            y = c + Solution.directions[i + 1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                area += self.dfs(grid, x, y)

        return area

if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    s = Solution()
    print(s.maxAreaOfIsland(grid))
