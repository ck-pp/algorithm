from collections import deque

def is_one_diff(word1, word2):
    diff_cnt = len([1 for a, b in zip(word1, word2) if a != b])
    return diff_cnt == 1

def solution(begin, target, words):
    # 가장 짧은 변환 과정 > 최단 거리 > BFS
    if target not in words:
        return 0
    
    words.append(begin)
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        cur_word, steps = queue.popleft()
        
        if cur_word == target:
            return steps
        
        for word in words:
            if word not in visited and is_one_diff(cur_word, word):
                visited.add(word)
                queue.append([word, steps + 1])
    return 0