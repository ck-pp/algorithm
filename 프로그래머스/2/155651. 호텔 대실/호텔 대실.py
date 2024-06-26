import heapq

def time_to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    books = []
    for start, end in book_time:
        start_time = time_to_minutes(start)
        end_time = time_to_minutes(end) + 10
        books.append((start_time, end_time))
        
    books.sort()
    heap = []
    
    for start, end in books:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        
    return len(heap)