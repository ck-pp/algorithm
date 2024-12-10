import sys
imput = sys.stdin.readline

N = int(input())
A_lists = list(map(int, input().split()))
B_lists = list(map(int, input().split()))

# A*B 곱의 합이 최소가 되려면 작은값*큰값으로 상쇄시켜야 한다.
sorted_A = sorted(A_lists)  # 오름차순
sorted_B = sorted(B_lists, reverse=True)  # 내림차순

sum_v = 0
for a, b in zip(sorted_A, sorted_B):
    sum_v += a*b
    
print(sum_v)