from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for word in goal:        
        # 카드1 뭉치에서 뽑은 카드가 원하는 단어인 경우
        if cards1 and cards1[0] == word:
            cards1.popleft()
        # 카드2 뭉치에서 뽑은 카드가 원하는 단어인 경우
        elif cards2 and cards2[0] == word:
            cards2.popleft()
        # 모든 카드 뭉치에 원하는 단어가 뽑히지 않은 경우
        else:
            return "No"
            
    return "Yes"