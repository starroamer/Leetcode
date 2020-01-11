class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        row_set = defaultdict(lambda: set())
        col_set = defaultdict(lambda: set())
        cell_set = defaultdict(lambda: set())
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                cell_id = (j // 3) + (i // 3) * 3
                if num in row_set[i] or num in col_set[j] or num in cell_set[cell_id]:
                    return False
                row_set[i].add(num)
                col_set[j].add(num)
                cell_set[cell_id].add(num)

        return True


if __name__ == "__main__":
    s = Solution()
    input = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(s.isValidSudoku(input))