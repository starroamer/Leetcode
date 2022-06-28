from typing import List

class Solution:
    """
    https://leetcode.cn/problems/can-place-flowers/
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        length = len(flowerbed)
        skip = False
        for i in range(length):
            if skip:
                skip = False
                continue
            current_ok = flowerbed[i] != 1
            left_ok = flowerbed[i - 1] != 1 if i > 0 else True
            right_ok = flowerbed[i + 1] != 1 if i < length - 1 else True
            if current_ok and left_ok and right_ok:
                flowerbed[i] = 1
                n -= 1
                skip = True

            if n == 0:
                break

        return n == 0


if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    s = Solution()
    print(s.canPlaceFlowers(flowerbed, n))
