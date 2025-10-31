class Leaderboard:

    def __init__(self):
        self.score_map = {}
        self.score_list = SortedList([], key = lambda x: 100-x[0])


    def addScore(self, playerId: int, score: int) -> None:
        prev_score = 0
        if playerId in self.score_map:
            # remove the previous score
            prev_score = self.score_map[playerId]
            self.score_list.remove((prev_score, playerId))

        # add new score
        new_score = score + prev_score
        self.score_map[playerId] = new_score
        self.score_list.add((new_score, playerId))


    def top(self, K: int) -> int:
        score_sum = 0
        for score, playerId in self.score_list[:K]:
            score_sum += score
        return score_sum


    def reset(self, playerId: int) -> None:
        if playerId in self.score_map:
            # remove the previous score
            prev_score = self.score_map[playerId]
            self.score_list.remove((prev_score, playerId))
            del self.score_map[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)