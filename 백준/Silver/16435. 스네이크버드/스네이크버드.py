import sys
input = sys.stdin.readline

N, L = map(int, input().split())  # 과일의 개수, 스네이크버드의 초기 길이
h = list(map(int, input().split()))

# 1. 각 과일의 높이 오름차순 정렬
h.sort()

# 2. 과일 먹어서 길이 늘리기
for i in range(len(h)):
    if h[i] <= L:
        L += 1
    
    else:
        break

# 3. 스네이크버드의 최대 길이 출력
print(L)