import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(input().strip() for _ in range(N))
strings = list(input().strip() for _ in range(M))

S.sort()
strings.sort()

ans = 0
for string in strings:
    if string in S:
        ans += 1
    
print(ans)