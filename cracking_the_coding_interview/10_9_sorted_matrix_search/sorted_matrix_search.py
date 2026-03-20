from typing import List

class Solution:
    """
    https://leetcode.cn/problems/sorted-matrix-search-lcci
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False

        i = n - 1
        j = 0
        while i >=0 and j < m:
            if target == matrix[j][i]:
                return True
            elif target < matrix[j][i]:
                i -= 1
            else:
                j += 1
            
        return False
        

if __name__   == "__main__":
    s = Solution()
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    m = [ [1, 1]
        # [1,   4,  7, 11, 15],
        # [2,   5,  8, 12, 19],
        # [3,   6,  9, 16, 22],
        # [10, 13, 14, 17, 24],
        # [18, 21, 23, 26, 30]
    ]
    target = 0
    print(s.searchMatrix(m, target))