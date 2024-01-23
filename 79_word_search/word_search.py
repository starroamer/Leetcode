class Solution:
    """
    https://leetcode.cn/problems/word-search/
    """
    from typing import List
    directions = [-1, 0, 1, 0, -1]
    def exist(self, board: List[List[str]], word: str) -> bool:
        wide = len(board[0])
        height = len(board)
        length = len(word)
        visited = [[False for i in range(wide)] for j in range(height)]
        for i in range(height):
            for j in range(wide):
                if self.check_exist(board, word, visited, i, j):
                    return True
        return False

    # 检查坐标(r, c)处是否能找到word
    def check_exist(self, board, word, visited, r, c):
        if board[r][c] == word[0] and len(word) == 1:
            return True
        elif board[r][c] != word[0]:
            return False
        visited[r][c] = True
        for i in range(4):
            x = r + Solution.directions[i]
            y = c + Solution.directions[i + 1]
            if x >= 0 and y >= 0 and x < len(board) and y < len(board[0]) and not visited[x][y]:
                if self.check_exist(board, word[1:], visited, x, y):
                    return True
        visited[r][c] = False
        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCFDEE"
    s = Solution()
    print(s.exist(board, word))