from collections import deque

def solution(people, limit):
    people = deque(sorted(people))  # 오름차순 정렬
    ans = 0
    
    while people:
        n = len(people)
        if n > 1 and people[0] + people[-1] <= limit:
            people.popleft()
        
        people.pop()
        ans += 1
        
    return ans