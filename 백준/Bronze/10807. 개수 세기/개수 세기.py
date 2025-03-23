import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
v = int(input())  # 찾으려고 하는 정수

# 각 정수의 개수 저장(카운트-딕셔너리)
num_cnts = Counter(nums)
# 주어진 N개의 정수 중에 v가 몇 개인지 출력
print(num_cnts[v])