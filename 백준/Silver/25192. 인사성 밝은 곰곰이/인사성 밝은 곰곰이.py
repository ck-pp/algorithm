import sys
input = sys.stdin.readline

N = int(input())
peoples = set([])

ans = 0
for _ in range(N):
    info = input().strip()
    if info == 'ENTER':
        peoples.clear()
    else:
        if info not in peoples:
            peoples.add(info)
            ans += 1

print(ans)