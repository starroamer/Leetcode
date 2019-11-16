class Solution(object):
    """
    https://leetcode-cn.com/problems/generate-parentheses/
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        init_seq = ""
        left_n = unmatch_left_n = 0
        self.do_generateParenthesis(results, n, init_seq, left_n, unmatch_left_n)

        return results

    def do_generateParenthesis(self, results, n, seq, left_num, unmatch_left_num):
        # print(seq, unmatch_left_num)
        if len(seq) == 2 * n:
            results.append(seq)
            return

        if left_num < n:
            new_seq_left = seq + "("
            self.do_generateParenthesis(results, n, new_seq_left, left_num + 1, unmatch_left_num + 1)

        if unmatch_left_num > 0:
            new_seq_right = seq + ")"
            self.do_generateParenthesis(results, n, new_seq_right, left_num, unmatch_left_num - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(4))
