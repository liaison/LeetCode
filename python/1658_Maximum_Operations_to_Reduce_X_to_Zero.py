

class SolutionTLE:
    def minOperations(self, nums: List[int], x: int) -> int:

        """
            TLE: time limit exceeded
        """
        # queue = deque([(x, left, right, 0)])
        queue = deque()
        queue.append((x, 0, len(nums)-1, 0))

        # BFS traversal
        while queue:
            remain, left, right, steps = queue.popleft()

            if remain == 0:
                return steps
            elif remain < 0:
                continue
            elif left > right:
                continue

            # try leftmost and rightmost
            queue.append((remain - nums[left], left+1, right, steps+1))
            queue.append((remain - nums[right], left, right-1, steps+1))


        return -1