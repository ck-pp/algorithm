import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque(range(1, N+1))
res = []

while q:
    # K-1번 회전하여 K번째 사람을 앞으로 보냄
    q.rotate(-(K - 1))
    # K번째 사람 제거 및 결과 저장
    res.append(q.popleft())

print("<" + ", ".join(map(str, res)) + ">")