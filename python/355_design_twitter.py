class Twitter:

    def __init__(self):
        # user -> [(timestamp, tweetId)]
        self.user_to_tweets_map = defaultdict(list)

        # follower -> set of followees
        self.follower_map = defaultdict(set)
        self._timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets_map[userId].append((self._timestamp, tweetId))
        self._timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        merged_tweets = self.user_to_tweets_map[userId][-10:]
        for followee in self.follower_map[userId]:
            followee_tweets = self.user_to_tweets_map[followee]
            merged_tweets.extend(followee_tweets[-10:])

        merged_tweets.sort(reverse = True)
        return [tweetId for timestamp, tweetId in merged_tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


class TwitterHeap:

    def __init__(self):
        # user -> [(timestamp, tweetId)]
        self.user_to_tweets_map = defaultdict(list)

        # follower -> set of followees
        self.follower_map = defaultdict(set)
        self._timestamp = 1


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets_map[userId].append((-self._timestamp, tweetId))
        self._timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        merged_tweets = self.user_to_tweets_map[userId][-10:]
        for followee in self.follower_map[userId]:
            followee_tweets = self.user_to_tweets_map[followee]
            merged_tweets.extend(followee_tweets[-10:])

        heapq.heapify(merged_tweets)
        top_tweets = []
        index = 0
        total_length = len(merged_tweets)
        while index < 10 and index < total_length:
            index += 1
            timestamp, most_recent_tweet = heapq.heappop(merged_tweets)
            top_tweets.append(most_recent_tweet)
        return top_tweets


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


class TwitterMergeSort:

    def __init__(self):
        # user -> [(timestamp, tweetId)]
        self.user_to_tweets_map = defaultdict(list)

        # follower -> set of followees
        self.follower_map = defaultdict(set)
        self._timestamp = 1


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets_map[userId].append((-self._timestamp, tweetId))
        self._timestamp += 1


    def merge_sort(self, tweets):
        top_tweets_heap = []
        for queue_index, tweet_list in enumerate(tweets):
            timestamp, tweet = tweet_list[0]
            queue_pointer = 1
            entry = (timestamp, tweet, queue_index, queue_pointer)
            heapq.heappush(top_tweets_heap, entry)

        count = 0
        results = []
        while count < 10 and top_tweets_heap:
            timestamp, tweet, queue_index, queue_pointer = heapq.heappop(top_tweets_heap)
            results.append(tweet)
            count += 1

            if queue_pointer < len(tweets[queue_index]):
                next_timestamp, next_tweet = tweets[queue_index][queue_pointer]
                next_entry = (next_timestamp, next_tweet, queue_index, queue_pointer + 1)
                heapq.heappush(top_tweets_heap, next_entry)

        return results

    def getNewsFeed(self, userId: int) -> List[int]:

        tweets = []
        for user in self.follower_map[userId] | set([userId]):
            user_tweets = self.user_to_tweets_map[user][-10:]
            user_tweets.reverse()
            if len(user_tweets) > 0:
                tweets.append(user_tweets)

        return self.merge_sort(tweets)


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)