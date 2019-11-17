class Solution(object):
    """
    https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
    """
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import defaultdict

        str_len = len(s)
        word_cnt_map = defaultdict(int)
        word_num = 0
        for word in words:
            word_cnt_map[word] += 1
            word_num += 1
        if str_len == 0 or word_num == 0:
            return []
        word_len = len(words[0])

        result = []
        cur_word_cnt_map = defaultdict(int)
        for i in range(str_len):
            cur_word_cnt_map.clear()
            if i + word_num * word_len > str_len:
                break

            not_match = False
            for j in range(word_num):
                sub_str = s[i + j * word_len:i + (j + 1) * word_len]
                cur_word_cnt_map[sub_str] += 1
                if cur_word_cnt_map[sub_str] > word_cnt_map[sub_str]:
                    not_match = True
                    break
            if not_match:
                continue
            result.append(i)

        return result


if __name__ == "__main__":
    s = Solution()
    input_str = "wordgoodbestgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    print(s.findSubstring(input_str, words))
