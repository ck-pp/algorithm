from collections import deque

# 1. 두 단어가 알파벳 한 개 차이인지 T/F 출력
def is_one_diff(word1, word2):
    diff_cnt = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff_cnt += 1
    
    return diff_cnt == 1

def solution(begin, target, words):
    
    # target으로 변환할 수 없는 경우
    if target not in words:
        return 0
    
    # 1. bfs 로직 실행
    q = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set([begin])  # 단어 방문 여부
    
    while q:
        cur_word, steps = q.popleft()
        
        if cur_word == target:
            break
        
        for next_word in words:
            # 방문한 적 없고, 현재 단어와 알파벳 한 개만 다를 경우
            if next_word not in visited and is_one_diff(cur_word, next_word):
                q.append((next_word, steps + 1))
                visited.add((next_word))
    
    # 2. begin -> target 변환 단계 출력
    return steps
    