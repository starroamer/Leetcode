class Solution:
    """
    https://leetcode-cn.com/problems/edit-distance/
    """
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        s = [[0] * len2 for _ in range(len1)]
        c = [[""] * len2 for _ in range(len1)]
        for i in range(len1):
            for j in range(len2):
                if i == 0:
                    s[i][j] = j
                    c[i][j] = '←'
                elif j == 0:
                    s[i][j] = i
                    c[i][j] = '↑'
                elif word1[i - 1] == word2[j - 1]:
                    s[i][j] = s[i - 1][j - 1]
                    c[i][j] = '\\'
                else:
                    min_s = min(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1])
                    s[i][j] = min_s + 1
                    if min_s == s[i - 1][j - 1]:
                        c[i][j] = '0'
                    if min_s == s[i - 1][j]:
                        c[i][j] = '↑'
                    elif min_s == s[i][j - 1]:
                        c[i][j] = '←'

        for i in s:
            print(" ".join(map(str, i)))
        for j in c:
            print(" ".join(map(str, j)))
        cur_str = word2
        str_list = [cur_str]
        i = len1 - 1
        j = len2 - 1
        while True:
            if c[i][j] == '←':
                print("b: %s" % cur_str)
                cur_str = cur_str[:j - 1] + cur_str[j:]
                print("a: %s" % cur_str)
                str_list.insert(0, cur_str)
                j -= 1
            elif c[i][j] == '↑':
                print("b: %s" % cur_str)
                cur_str = cur_str[:j] + word1[i - 1] + cur_str[j:]
                print("a: %s" % cur_str)
                str_list.insert(0, cur_str)
                i -= 1
            else:
                if c[i][j] == '0':
                    print("b: %s" % cur_str)
                    print("replace: %s -> %s" % (cur_str[j - 1], word1[i - 1]))
                    cur_str = cur_str[:j - 1] + word1[i - 1] + cur_str[j:]
                    print("a: %s" % cur_str)
                    str_list.insert(0, cur_str)
                i -= 1
                j -= 1
            if i < 1 or j < 1:
                break

        print(" ".join(str_list))

        return s[len1 - 1][len2 - 1]


if __name__ == "__main__":
    solution = Solution()
    str1 = "contract"
    str2 = "intent"
    d = solution.minDistance(str1, str2)
    print(d)
