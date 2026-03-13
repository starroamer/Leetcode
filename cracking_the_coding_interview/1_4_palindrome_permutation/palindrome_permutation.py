class Solution:
    """
    https://leetcode.cn/problems/palindrome-permutation-lcci/
    """
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                del dic[c]

        return len(dic) <= 1

        
if __name__   == "__main__":
    s = Solution()
    input = "abaac"
    print(s.canPermutePalindrome(input))