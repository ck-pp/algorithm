from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))  # 내림차순 정렬
    ans = 0
    
    while people:
        n = len(people)
        # 두 명의 무게 합이 limit 이하이면, 두 명 다 배열에서 제거한다.
        if n > 1 and people[0] + people[-1] <= limit:
            people.pop()
        
        people.popleft()
        ans += 1
        
    return ans