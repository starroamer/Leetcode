class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row_num = [set(map(str, range(1, 10))) for _ in range(9)]
        col_num = [set(map(str, range(1, 10))) for _ in range(9)]
        block_num = [set(map(str, range(1, 10))) for _ in range(9)]

        empty_cell = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    row_num[i].remove(element)
                    col_num[j].remove(element)
                    block_num[(i // 3) * 3 + j // 3].remove(element)
                else:
                    empty_cell.append([i, j, 0])
        for cell in empty_cell:
            i, j = cell[:2]
            block_empty_num = len(block_num[(i // 3) * 3 + j // 3])
            cell[2] = block_empty_num
        print(empty_cell)
        empty_cell.sort(key=lambda x: x[2])
        print(empty_cell)

        def backtrace(iter):
            if iter == len(empty_cell):
                return True
            i, j = empty_cell[iter][:2]
            cell_id = (i // 3) * 3 + j // 3
            for num in row_num[i] & col_num[j] & block_num[cell_id]:
                board[i][j] = num
                row_num[i].remove(num)
                col_num[j].remove(num)
                block_num[cell_id].remove(num)
                if backtrace(iter + 1):
                    return True
                row_num[i].add(num)
                col_num[j].add(num)
                block_num[cell_id].add(num)
            return False
        backtrace(0)


if __name__ == "__main__":
    s = Solution()
    input = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(input)
    print(input)