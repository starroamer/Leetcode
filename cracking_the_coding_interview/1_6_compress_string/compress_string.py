class Solution:
    """
    https://leetcode.cn/problems/compress-string-lcci
    """
    def compressString(self, S: str) -> str:
        length = len(S)
        if length == 0:
            return S
        current = S[0] 
        sub_len = 1
        result = []
        result_len = 0
        for i in range(1, length):
            if S[i] == current:
                sub_len += 1
            else:
                result.append(f'{current}{sub_len}')
                result_len += 2
                current = S[i]
                sub_len = 1
        result.append(f'{current}{sub_len}')
        result_len += 2
        result = "".join(result)

        if result_len < length:
            return result
        else:
            return S
        
if __name__   == "__main__":
    s = Solution()
    input = "aabbccc"
    print(s.compressString(input))