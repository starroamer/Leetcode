class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/coin-change
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)

        # amount等于coins中的某个金额，最少只需一个硬币
        for i in coins:
            if i <= amount:
                dp[i] = 1

        for i in range(1, amount + 1):
            solution_list = []

            # 已经确定只需要一个硬币的情况，不改动
            if dp[i] > 0:
                continue

            # 要凑足金额i, 可行方案为先凑足i-v的金额, 再使用一个面额为v的硬币, 即dp[i - v] + 1
            # 对不同的v, 取上述解的最小值
            for value in coins:
                if value < i and dp[i - value] > 0:
                    solution_list.append(dp[i - value])
                if solution_list:
                    dp[i] = min(solution_list) + 1

        return dp[amount]

    def coinChangeV2(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        max_value = max(coins)
        dp = []

        for i in range(1, amount + 1):
            if len(dp) >= max_value + 1:
                dp.pop(0) 

            dp.append(-1)
            # amount等于coins中的某个金额，最少只需一个硬币
            if i in coins:
                dp[-1] = 1
            else:
                solution_list = []

                # 要凑足金额i, 可行方案为先凑足i-v的金额, 再使用一个面额为v的硬币, 即dp[i - v] + 1
                # 对不同的v, 取上述解的最小值
                for value in coins:
                    print("i: ", i, "value: ", value, "dp: ", dp)
                    if value <= len(dp) - 1 and dp[-1 - value] > 0:
                        solution_list.append(dp[-1 - value])
                    print("solutions: ", solution_list)
                if solution_list:
                    dp[-1] = min(solution_list) + 1

            print("i: ", i, "dp: ", dp)

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(solution.coinChangeV2(coins, amount))
