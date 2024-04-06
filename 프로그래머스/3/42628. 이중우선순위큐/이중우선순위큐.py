from collections import deque
import heapq as hq

def solution(operations):
    min_heap = []
    max_heap = []
    for i in operations:
        oper, num = i.split(' ')
        if oper == 'I':
            hq.heappush(min_heap, int(num))
            hq.heappush(max_heap, -int(num))
        else:
            if num == '-1' and min_heap != []:
                x = hq.heappop(min_heap)
                max_heap.remove(-x)
            elif num == '1' and max_heap != []:
                x = hq.heappop(max_heap)
                min_heap.remove(-x)
    if len(min_heap) == 0:
        return [0, 0]
    return [-hq.heappop(max_heap), hq.heappop(min_heap)]