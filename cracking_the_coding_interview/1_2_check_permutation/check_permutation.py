class Solution:
    """
    https://leetcode.cn/problems/check-permutation-lcci/description
    """
    def checkPermutation(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if len(s2) != length:
            return False
        a = [0] * 26
        for i in range(length):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')
            a[idx1] = a[idx1] + 1
            a[idx2] = a[idx2] - 1

        return not any(a)

        
if __name__   == "__main__":
    s = Solution()
    s1 = "abc"
    s2 = "bac"
    print(s.checkPermutation(s1, s2))