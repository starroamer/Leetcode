from typing import List

class Solution:
    """
    https://leetcode.cn/problems/zero-matrix-lcci/
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        n = len(matrix)
        m = len(matrix[0])
        if m == 0: return
        row_s = set()
        col_s = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_s.add(i)
                    col_s.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in row_s or j in col_s:
                    matrix[i][j] = 0
        
        
if __name__   == "__main__":
    s = Solution()
    matrix = [
        [0,0,0,5],
        [4,3,1,4],
        [0,1,1,4],
        [1,2,1,3],
        [0,0,1,1]
    ]
    s.setZeroes(matrix)
    for row in matrix:
        print(row)