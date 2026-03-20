from typing import List

class Solution:
    """
    https://leetcode.cn/problems/sorted-merge-lcci
    """
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i = m - 1
        j = n - 1
        p = m + n -1
        while i >= 0 and j >= 0:
            A[p] = max(A[i], B[j])
            if A[i] >= B[j]:
                i -= 1
            else:
                j -= 1
            p -= 1

        while j >= 0:
            A[p] = B[j]
            p -= 1
            j -= 1
        
        
if __name__   == "__main__":
    s = Solution()
    A = [1,2,3,0,0,0]
    m = 3
    B = [2,5,6]
    n = 3
    s.merge(A, m, B, n)
    print(A)