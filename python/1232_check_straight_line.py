class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        def angle(start, end):
            start_x, start_y = start[0], start[1]
            end_x, end_y = end[0], end[1]
            x_offset = end_x - start_x
            y_offset = end_y - start_y
            if y_offset == 0:
                # avoid division by zero
                return float('inf')
            return float(x_offset) / y_offset

        start_angle = angle(coordinates[0], coordinates[1])

        start_point = coordinates[0]
        for index in range(2, len(coordinates)):
            next_angle = angle(coordinates[index], start_point)
            if next_angle != start_angle:
                return False

        return True


    def checkStraightLine_vector(self, coordinates: List[List[int]]) -> bool:
        """
            Using the vector representation, to avoid the division-by-zero

            x_1/y_1 == x_2/y_2 ---> (x_1 * y_2) == (x_2 * y_1)

        """
        def angle_vector(start, end):
            start_x, start_y = start[0], start[1]
            end_x, end_y = end[0], end[1]
            x_offset = end_x - start_x
            y_offset = end_y - start_y
            return (x_offset, y_offset)

        def is_equal_vector(vec_one, vec_other):
            x_one, y_one = vec_one
            x_other, y_other = vec_other
            return (x_one * y_other) == (x_other * y_one)

        start_angle = angle_vector(coordinates[0], coordinates[1])
        start_point = coordinates[0]
        for index in range(2, len(coordinates)):
            next_angle = angle_vector(coordinates[index], start_point)

            if not is_equal_vector(start_angle, next_angle):
                return False

        return True
