class FileSharing:

    def __init__(self, m: int):
        self.user_to_chunks = defaultdict(set)
        self.chunk_to_users = defaultdict(set)
        self.available_user_id = []
        self.user_id_count = 0

    def join(self, ownedChunks: List[int]) -> int:
        if not self.available_user_id:
            user_id = self.user_id_count + 1
            self.user_id_count += 1
        else:
            user_id = heapq.heappop(self.available_user_id)

        self.user_to_chunks[user_id] = set(ownedChunks)

        for chunk_id in ownedChunks:
            self.chunk_to_users[chunk_id].add(user_id)

        return user_id


    def leave(self, userID: int) -> None:
        # release chunks
        for chunk_id in self.user_to_chunks[userID]:
            self.chunk_to_users[chunk_id].remove(userID)

        del self.user_to_chunks[userID]

        # recycle user_id
        heapq.heappush(self.available_user_id, userID)


    def request(self, userID: int, chunkID: int) -> List[int]:

        curr_owners = self.chunk_to_users[chunkID].copy()

        # if the chunk DOES NOT exist, then do NOT allocate
        if curr_owners:
            # allocate the increased chunk
            self.user_to_chunks[userID].add(chunkID)
            self.chunk_to_users[chunkID].add(userID)

        return sorted(curr_owners)


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)