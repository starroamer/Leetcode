class Solution(object):
    """
    https://leetcode-cn.com/problems/zigzag-conversion/
    """
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        import math
        s_len = len(s)
        unit_len = 2 * (numRows - 1)
        n = math.ceil(s_len / unit_len)

        result = ""
        for i in range(numRows):
            line = ""
            for j in range(n):
                sub_str = [" "] * (numRows - 1)
                idx1 = i + j * unit_len
                if idx1 < s_len:
                    sub_str[0] = s[idx1]
                if i != 0 and i != numRows - 1:
                    k = numRows - 1 - i
                    idx2 = idx1 + unit_len - 2 * i
                    if idx2 < s_len:
                        sub_str[k] = s[idx2]

                line += "".join(sub_str)
            print(line)
            result += line
        return result.replace(" ", "")


if __name__ == "__main__":
    s = Solution()
    string = "LEETCODEISHIRING"
    n = 5
    print(s.convert(string, n))
