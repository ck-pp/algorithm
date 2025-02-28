import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
C = input().strip()

# 수로 생각했을 때, A+B-C 출력
print(int(A) + int(B)- int(C))

# 문자열로 생각했을 때, A+B-C 출력
print(int(A + B) - int(C))