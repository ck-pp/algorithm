import sys
from collections import Counter
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

multiple_value = A * B * C
number_cnt = Counter(str(multiple_value))
sorted_num_cnt = sorted(number_cnt.items(), key=lambda item:item[0])

ans = [0 for _ in range(10)]
for i, cnt in sorted_num_cnt:
    ans[int(i)] = cnt

for c in ans:
    print(c)