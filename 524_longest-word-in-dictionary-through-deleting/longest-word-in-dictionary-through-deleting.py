class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/
    """
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        s_len = len(s)
        # 将dictionary按字符串长度排序，长度相同的字符串按字典顺序排序
        dictionary.sort(key=lambda x: (-len(x), x))

        # 遍历dictionary，返回第一个满足要求的字符串
        for word in dictionary:
            word_len = len(word)
            if word_len > s_len:
                continue
            i = 0
            for j in range(s_len):
                if s[j] == word[i]:
                    if i == word_len - 1: 
                        return word
                    else:
                        i += 1

        return ""

if __name__ == "__main__":
    s = Solution()
    str = "abpcplea"
    dictionary = ["ale","apple","monkey","plea"]
    print(s.findLongestWord(str, dictionary))
