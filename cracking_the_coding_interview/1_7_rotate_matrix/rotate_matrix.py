from typing import List

class Solution:
    """
    https://leetcode.cn/problems/rotate-matrix-lcci
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N < 2: return

        # 转置
        for i in range(1, N):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 左右翻转
        for i in range(0, N):
            matrix[i].reverse()


        
        
if __name__   == "__main__":
    s = Solution()
    matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    s.rotate(matrix)
    for row in matrix:
        print(row)