import sys
input = sys.stdin.readline

N = int(input())
x_y_lists = [list(map(int, input().split())) for _ in range(N)]

x_y_lists.sort(key=lambda x:(x[0], x[1]))

for x, y in x_y_lists:
    print(str(x) + ' ' + str(y))