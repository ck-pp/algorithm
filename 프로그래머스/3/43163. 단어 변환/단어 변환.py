# 최단경로 -> BFS(큐)
from collections import deque

def is_one_diff(w1, w2):
    diff_cnt = sum([1 for a, b in zip(w1, w2) if a != b])
    return diff_cnt == 1

def solution(begin, target, words):
    words.append(begin)
    q = deque([begin])
    visited = set([begin])
    dist = {begin: 0}
    
    while q:
        cur_word = q.popleft()
        
        if cur_word == target:
            return dist[cur_word]
        
        for next_word in words:
            if next_word not in visited and is_one_diff(cur_word, next_word):
                q.append(next_word)
                visited.add(next_word)
                dist[next_word] = dist[cur_word] + 1
    
    return 0