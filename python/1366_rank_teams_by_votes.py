class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        rank_counts = {}

        total_votes = len(votes)
        num_teams = len(votes[0])

        for vote in votes:
            for rank, name in enumerate(vote):
                if name not in rank_counts:
                    rank_counts[name] = defaultdict(int)
                keys = rank_counts[name]
                keys[rank] += 1

        rank_keys = []
        for name, counts in rank_counts.items():
            compound_key = []
            for position in range(num_teams):
                compound_key.append(str(total_votes - counts[position]))
            compound_key.append(name)

            rank_keys.append(("".join(compound_key), name))

        final_rank = sorted(rank_keys, key = lambda x:x[0])
        return "".join([name for _, name in final_rank])

