class Solution:
    """
    https://leetcode.cn/problems/one-away-lcci/
    """
    def oneEditAway(self, first: str, second: str) -> bool:
        l1 = len(first)
        l2 = len(second)
        
        if abs(l1 - l2) > 1:
            return False

        # 其中一个字符串为空, 另一个字符串为空或者为单个字符
        if l1 + l2 <= 1:
            return True

        # first固定为长度较长的字符串
        if l1 < l2:
            first, second = second, first
            l1 = len(first)
            l2 = len(second)

        p1 = 0
        p2 = 0
        edit = False
        offset = 0
        for i in range(l2):
            if first[i + offset] == second[i]:
                continue
            elif edit:
                return False
            else:
                edit = True
                # 插入一个字符的情况，指向first的指针后移一位
                if l1 != l2:
                    if first[i + offset + 1] == second[i]:
                        offset += 1
                    else:
                        return False

        return True

        
if __name__   == "__main__":
    s = Solution()
    first = "acm"
    second = "abcm"
    print(s.oneEditAway(first, second))