
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        """
            TLE at the 132/148 test cases
        """
        age_score = [(age, score) for age, score in zip(ages, scores)]
        age_score.sort(key = lambda x: x)
        age_score.append((0, 0))  # an artificial point as boundary

        @functools.lru_cache(maxsize=None)
        def dfs(curr_index, last_index):

            if curr_index == len(scores):
                return 0

            last_age, last_score = age_score[last_index]
            curr_age, curr_score = age_score[curr_index]

            max_score = 0
            if curr_age == last_age or curr_score >= last_score:
                # can add this person to the current team
                option1 = curr_score + dfs(curr_index+1, curr_index)
                max_score = max(max_score, option1)

            # skip this person
            option2 = dfs(curr_index+1, last_index)
            max_score = max(max_score, option2)

            #print(curr_index, last_index, max_score)
            return max_score

        return dfs(0, len(scores))


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        """
            Another TLE solution
        """
        age_score = [(age, score) for age, score in zip(ages, scores)]
        age_score.sort(key = lambda x: x)
        age_score.append((0, 0))  # an artificial point as boundary

        dp = dict()
        N = len(scores)
        for last_index in range(N+1):
            dp[(N, last_index)] = 0

        last_index = N
        for curr_index in range(N-1, -1, -1):
            for last_index in range(N, -1, -1):
                last_age, last_score = age_score[last_index]
                curr_age, curr_score = age_score[curr_index]

                max_score = 0
                if curr_age == last_age or curr_score >= last_score:
                    # can add this person to the current team
                    option1 = curr_score + dp[(curr_index+1, curr_index)]
                    max_score = max(max_score, option1)

                # skip this person
                option2 = dp[(curr_index+1, last_index)]
                max_score = max(max_score, option2)
                dp[(curr_index, last_index)] = max_score

        return dp[(0, N)]


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        age_score = [(age, score) for age, score in zip(ages, scores)]
        age_score.sort(key = lambda x: x)

        N = len(scores)
        # dp[i]:  maximum score for a team
        #         including "i" with all other possible members before ith element
        dp = [0] * N

        global_max = 0

        for curr_index in range(0, N):

            curr_age, curr_score = age_score[curr_index]
            max_score = curr_score

            for prev_index in range(0, curr_index):
                prev_age, prev_score = age_score[prev_index]

                if prev_score <= curr_score:
                    max_score = max(max_score, curr_score + dp[prev_index])

            dp[curr_index] = max_score
            global_max = max(global_max, max_score)


        return global_max
