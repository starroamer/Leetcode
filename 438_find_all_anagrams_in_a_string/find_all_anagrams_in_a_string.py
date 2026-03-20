from typing import List

class Solution:
    """
    https://leetcode.cn/problems/find-all-anagrams-in-a-string
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)
        ans = []
        if n1 < n2:
            return ans

        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(n2):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(n1 - n2):
            s_count[ord(s[i]) - ord('a')] -= 1
            s_count[ord(s[i + n2]) - ord('a')] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    s1 = "cbaebabacd"
    s2 = "abc"
    print(s.findAnagrams(s1, s2))