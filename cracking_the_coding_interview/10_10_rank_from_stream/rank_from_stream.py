class StreamRank:

    def __init__(self):
        from collections import defaultdict
        self.min_num = float('inf')
        self.rank_dict = defaultdict(int)

    def track(self, x: int) -> None:
        self.rank_dict[x] += 1
        if x < self.min_num:
            self.min_num = x

    def getRankOfNumber(self, x: int) -> int:
        rank = 0
        if self.min_num == float('inf'):
            return rank
        for i in range(self.min_num, x + 1):
            rank += self.rank_dict[i]
        return rank

if __name__   == "__main__":
    obj = StreamRank()
    print(obj.getRankOfNumber(1))
    obj.track(0)
    print(obj.getRankOfNumber(0))