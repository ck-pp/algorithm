import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
name_ranks = [len(input().strip()) for _ in range(N)]  # 이름 길이만 저장

# 좋은 친구 = 등수의 차이가 K보다 작거나 같으면서 이름의 길이가 같은 친구
# 슬라이딩 윈도우 + 해시맵
count_map = defaultdict(int)  # 키가 처음 접근되면, 기본값이 0으로 초기화
cnt = 0
for i in range(N):
    if i > K:  # 슬라이딩 윈도우가 범위 벗어나면 제거
        count_map[name_ranks[i - K - 1]] -= 1
    
    cnt += count_map[name_ranks[i]]
    
    count_map[name_ranks[i]] += 1  # 현재 이름 길이 -> 슬라이딩 윈도우에 추가
        

print(cnt)