

class Solution:
    def reorganizeString(self, s: str) -> str:

        char_cnt = defaultdict(int)
        for char in s:
            char_cnt[char] += 1

        heap_queue = []
        for char, cnt in char_cnt.items():
            heap_queue.append((-cnt, char))

        heapq.heapify(heap_queue)

        char_list = []

        while len(heap_queue) > 1:
            # alternate the top two common letters
            cnt_1st, char_1st = heapq.heappop(heap_queue)
            cnt_2nd, char_2nd = heapq.heappop(heap_queue)

            if abs(cnt_1st) > abs(cnt_2nd):
                match_cnt = abs(cnt_2nd)
                heapq.heappush(heap_queue, (cnt_1st-cnt_2nd, char_1st))
            elif abs(cnt_1st) == 1:
                match_cnt = 1
            else: # cnt_1st == cnt_2nd
                # A different strategy to handle the specific cases
                # test case:  aabbcc -->  ab ac bc
                match_cnt = abs(cnt_1st) - 1
                heapq.heappush(heap_queue, (-1, char_1st))
                heapq.heappush(heap_queue, (-1, char_2nd))

            for _ in range(match_cnt):
                char_list.append(char_1st)
                char_list.append(char_2nd)


        if len(heap_queue) == 0:
            return "".join(char_list)
        else:
            last_cnt, last_char = heapq.heappop(heap_queue)
            if abs(last_cnt) > 1:
                return ""

            char_list.append(last_char)
            return "".join(char_list)

