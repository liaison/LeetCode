
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        mono_stack = []
        answer = [0] * len(T)

        for index, number in enumerate(T):

            while mono_stack:
                top_index, top_number = mono_stack[-1]
                if top_number < number:
                    mono_stack.pop()
                    answer[top_index] = index - top_index
                else:
                    break

            mono_stack.append((index, number))

        return answer