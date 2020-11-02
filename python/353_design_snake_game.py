class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = deque([(item[0], item[1]) for item in food])
        self.snake = deque([(0, 0)])
        self.offsets = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    
    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        row_offset, col_offset = self.offsets[direction]
        row, col =  self.snake[0] # head of snake
        new_row, new_col = row + row_offset, col + col_offset
                
        if new_row < 0 or new_row >= self.height \
            or new_col < 0 or new_col >= self.width:
            return -1
        
        if len(self.food) > 0 and (new_row, new_col) == self.food[0]:
            self.food.popleft()
        else:
            self.snake.pop()
            if (new_row, new_col) in self.snake:
                return -1
        
        self.snake.appendleft((new_row, new_col))
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)