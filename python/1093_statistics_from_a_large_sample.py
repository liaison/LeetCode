
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        num_count = []
        for num, count in enumerate(count):
            if count != 0:
                num_count.append((num, count))

        output = []
        # minimum
        output.append(num_count[0][0])
        # maximum
        output.append(num_count[-1][0])

        total_sum = 0
        total_count = 0
        max_count = 0
        mode = 0
        for (num, count) in num_count:
            total_sum += num * count
            total_count += count
            if count > max_count:
                mode = num
                max_count = count

        # mean
        output.append(total_sum / total_count)

        mid_index = total_count // 2
        prefix_sum = 0
        for index, (num, count) in enumerate(num_count):
            prefix_sum += count
            if mid_index <= prefix_sum:
                break

        # median
        if total_count % 2 == 0:
            # even number
            if mid_index == prefix_sum:
                median = (num + num_count[index+1][0]) / 2
            else:
                median = num

            output.append(median)
        else:
            # odd number
            if mid_index == prefix_sum:
                output.append(num_count[index+1][0])
            else:
                output.append(num)


        # mode
        output.append(mode)

        return output


