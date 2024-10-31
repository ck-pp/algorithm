import sys
from collections import Counter

N = int(sys.stdin.readline())
book_sales = [sys.stdin.readline().strip() for _ in range(N)]

count_sales = Counter(book_sales)
sorted_sales = sorted(count_sales.items(), key=lambda x:(-x[1], x[0]))
# 첫번째 기준 -x[1]: 팔린 개수 기준 내림차순
# 두번째 기준 x[0]: 이름 사전순(오름차순)

print(sorted_sales[0][0])