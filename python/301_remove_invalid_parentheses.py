class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(expr):
            balance = 0
            for char in expr:
                if char not in '()':
                    continue

                if char == "(":
                    balance += 1
                elif char == ")":
                    balance -= 1

                if balance < 0:
                    return False
            return balance == 0

        queue = deque([s])
        visited = set([s])
        found = False
        output = []

        while queue:
            substr = queue.popleft()

            if is_valid(substr):
                output.append(substr)
                found = True

            if found:
                continue

            for index in range(len(substr)):
                if substr[index] not in "()":
                    continue
                new_str = substr[:index] + substr[index+1:]
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)

        return output



