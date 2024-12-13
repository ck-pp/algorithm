import sys
imput = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
x = int(input())

sorted_seq = sorted(sequence)
i, j = 0, n-1
cnt = 0

while i < j:
    sum_v = sorted_seq[i] + sorted_seq[j]
    if sum_v == x:
        cnt += 1
        i += 1
        j -= 1
    elif sum_v < x:
        i += 1
    else:
        j -= 1

print(cnt)