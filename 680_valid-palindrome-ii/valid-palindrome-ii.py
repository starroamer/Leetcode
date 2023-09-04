class Solution:
    """
    https://leetcode.cn/problems/valid-palindrome-ii
    """
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return self.isPalindrome(s, l, r - 1) or self.isPalindrome(s, l + 1, r)

        return l >= r
    
    def isPalindrome(self, s, start, end) -> bool:
        l = start
        r = end
        while (l < r - 1):
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                break
        
        return s[l] == s[r]


if __name__ == "__main__":
    input = "abcba"
    s = Solution()
    print(s.validPalindrome(input))
