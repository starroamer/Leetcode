from typing import List

class Solution:
    """
    https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
        sorted_list = sorted(points, key=lambda x: x[1])
        min_arrow_cnt = 1
        prev = sorted_list[0][1]
        for i in range(1, n):
            if (sorted_list[i][0] > prev):
                prev = sorted_list[i][1]
                min_arrow_cnt += 1

        return min_arrow_cnt


if __name__ == "__main__":
    # points = [[10,16],[2,8],[1,6],[7,12]]
    # points = [[1,2],[3,4],[5,6],[7,8]]
    points = [[1,2],[2,3],[3,4],[4,5]]
    s = Solution()
    print(s.findMinArrowShots(points))
