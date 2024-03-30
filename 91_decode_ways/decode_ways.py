class Solution:
    """
    https://leetcode.cn/problems/decode-ways
    """
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        str_len = len(s)
        pre_1 = 1
        pre_2 = 0
        result = pre_1

        for i in range(1, str_len):
            result = 0
            n1 = int(s[i])
            if n1 != 0:
                result = pre_1
            n2 = int(s[i - 1:i + 1])
            if n2 >= 10 and n2 <= 26:
                if i == 1:
                    result += 1
                else:
                    result += pre_2

            pre_2 = pre_1
            pre_1 = result
            
        return result

if __name__ == "__main__":
    s = Solution()
    input= "10"
    print(s.numDecodings(input))
