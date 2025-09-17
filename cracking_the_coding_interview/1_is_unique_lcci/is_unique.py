class Solution:
    """
    https://leetcode.cn/problems/is-unique-lcci/description
    """
    def isUnique(self, astr: str) -> bool:
        bitmap = 0
        i = 0
        for c in astr:
            if i > 26:
                return False
            idx = ord(c) - ord('a')
            bit = bitmap & (1 << idx)
            if bit != 0:
                return False
            bitmap = bitmap | (1 << idx)
            i += 1
        return True

        
if __name__   == "__main__":
    s = Solution()
    input = "acbd"
    print(s.isUnique(input))