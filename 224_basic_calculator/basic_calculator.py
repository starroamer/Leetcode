class Solution:
    """
    https://leetcode.cn/problems/basic-calculator
    双栈法，支持加减乘除括号运算
    """
    def calculate(self, s: str) -> int:
        import math
        op_pri = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "(": math.inf
        }
        num_stack = []
        op_stack = []

        # 始终以数字开头
        if s[0] != '-':
            s = "0+" + s 
        else:
            s = "0" + s

        i = 0
        str_length = len(s)
        pre_token = ""
        while i < str_length:
            c = s[i]
            print(f"iter start, index={i}, char={c}")
            if s[i].isdigit():
                # 数字部分，解析数字并入数字栈
                num, next = self.parse_num(s, i, str_length)
                num_stack.append(num)
                i = next
                pre_token = num
            else:
                # 运算符及括号解析
                if c == " ":
                    pass # do nothing
                elif c == "(":
                    # 左括号前面的运算都不能提前进行，直接入栈
                    op_stack.append(c)
                elif c == ")":
                    # 右括号前面的运算都可以提前进行，直到遇到对应的左括号
                    assert(len(op_stack) > 0)
                    op = op_stack.pop()
                    second = num_stack.pop()
                    while op != "(":
                        first = num_stack.pop()
                        print(f"handle ), first={first}, second={second}, op={op}")
                        second = self.calcu_two_num(first, second, op)
                        print(f"handle ), new second={second}")
                        print(f"hanlde ), num_stack: {num_stack}")
                        print(f"handle ), op_stack: {op_stack}")
                        if len(op_stack) == 0:
                            break
                        op = op_stack.pop()
                    num_stack.append(second)
                else:
                    # 当前运算符优先级不高于前一个运算符，则前一个运算符的计算可以提前进行
                    if len(op_stack) > 0:
                        pre_op = op_stack[-1]
                        if c == "-" and pre_token == "(":
                            # 处理(-2)这种情况，转换为(0-2)
                            num_stack.append(0)
                        if pre_op != "(" and op_pri[c] <= op_pri[pre_op]:
                            second = num_stack.pop()
                            while len(op_stack) > 0 and op_stack[-1] != "(" and op_pri[c] <= op_pri[op_stack[-1]]:
                                op = op_stack.pop()
                                first = num_stack.pop()
                                print(f"handle {c}, first={first}, second={second}, op={op}")
                                second = self.calcu_two_num(first, second, op)
                                print(f"handle {c}, new second={second}")
                                print(f"hanlde {c}, num_stack: {num_stack}")
                                print(f"handle {c}, op_stack: {op_stack}")
                            num_stack.append(second)
                    # 运算符入栈
                    op_stack.append(c)
                if c != " ":
                    pre_token = c
                i += 1

            print(f"iter done, index={i}, char={c}")
            print(f"num_stack: {num_stack}")
            print(f"op_stack: {op_stack}")

        # 运算符栈的出栈顺序已经和运算优先级一致，分别将运算符和数字出栈，计算最终结果
        # 取数字栈栈顶两个元素: second 和 first，运算符栈顶一个元素op, 计算 first op second
        # 计算结果作为数字栈新的栈顶
        assert(len(num_stack) == len(op_stack) + 1)
        second = num_stack.pop()
        while len(op_stack) > 0:
            first = num_stack.pop()
            op = op_stack.pop()
            second = self.calcu_two_num(first, second, op)

        return second

    def calcu_two_num(self, first, second, op):
        assert(op in ['+', '-', '*', '/'])
        if op == "+":
            return first + second
        elif op == "-":
            return first - second
        elif op == "*":
            return first * second
        elif op == "/":
            return int(first / second)

        return 0

    def parse_num(self, s, start, str_length):
        num = 0
        i = start
        while i < str_length and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        return num, i

if __name__ == "__main__":
    s = Solution()
    input = "((11+33) / 11 - 2* 4) * (8-3)"
    print("calculate result: ", s.calculate(input))
    print("actual result: ", eval(input))
