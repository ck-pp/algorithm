from collections import deque

def solution(people, limit):
    ans = max_idx = 0
    people = deque(sorted(people, reverse=True))
    
    while people:
        if len(people) > 1 and people[-1] + people[max_idx] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        ans += 1
    return ans