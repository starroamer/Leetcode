from typing import List

class Solution:
    """
    https://leetcode.cn/problems/partition-labels/
    """
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict
        result = []
        stat_dict = defaultdict(int)
        cur_dict = defaultdict(int)
        for c in s:
            stat_dict[c] += 1
        n = len(s)
        prev = -1
        for i in range(n):
            c = s[i]
            cur_dict[c] += 1

            # 当前字符已经全部包含在当前串中
            if cur_dict[c] == stat_dict[c]:
                del cur_dict[c]
                if not cur_dict:
                    # 当前串中的所有字符都只出现在当前串中
                    result.append(i - prev)
                    prev = i

        return result


if __name__ == "__main__":
    S = ""
    s = Solution()
    print(s.partitionLabels(S))
