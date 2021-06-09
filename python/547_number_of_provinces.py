class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def isExplored(node, visited):
            """
                To explore the province starting from the current node.
                Mark all connected cities as visited.

                return: True if the current city is visited already.
                    otherwise false.
            """
            if visited[node]:
                return True

            visited[node] = True
            is_connected = isConnected[node]
            for neighbor in range(0, city_num):
                if is_connected[neighbor] == 1 and not visited[neighbor]:
                    isExplored(neighbor, visited)

            return False

        city_num = len(isConnected)
        visited = [False for _ in range(city_num)]

        province_cnt = 0
        for city in range(city_num):
            if not isExplored(city, visited):
                province_cnt += 1

        return province_cnt
