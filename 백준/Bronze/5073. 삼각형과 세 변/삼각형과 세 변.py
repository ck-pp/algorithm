import sys

while True:
    a, b, c = sorted(list(map(int, sys.stdin.readline().split())))
    
    # 0 0 0인 경우 종료
    if a + b + c == 0:
        break
    
    if a + b <= c:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b != c:
        print("Scalene")
    else:
        print("Isosceles")