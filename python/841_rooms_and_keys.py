class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def dfs(curr):
            nonlocal visited

            visited.add(curr)
            for next_room in rooms[curr]:
                if next_room not in visited:
                    dfs(next_room)

        # kick off the traversal
        dfs(0)

        return len(visited) == len(rooms)
