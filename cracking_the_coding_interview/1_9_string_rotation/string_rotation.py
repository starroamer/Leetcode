from typing import List

class Solution:
    """
    https://leetcode.cn/problems/string-rotation-lcci/
    """
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2: return False
        for i in range(n1):
            sub1 = s1[:i]
            sub2 = s1[i:]
            new_s = sub2 + sub1
            if new_s == s2:
                return True
        return False
        
        
if __name__   == "__main__":
    s = Solution()
    s1 = ""
    s2 = "erbottlewaa"
    print(s.isFlipedString(s1, s2))