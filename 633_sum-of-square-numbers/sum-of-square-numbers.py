class Solution:
    """
    https://leetcode.cn/problems/sum-of-square-numbers/
    """
    def judgeSquareSum(self, c: int) -> bool:
        import math
        ret = False
        l = 0
        r = int(math.sqrt(c))
        while (l <= r):
            current_sum = l * l + r * r
            if current_sum == c:
                ret = True
                break
            elif current_sum < c:
                l += 1
            else:
                r -= 1

        return ret


if __name__ == "__main__":
    c = 123245
    s = Solution()
    print(s.judgeSquareSum(c))
