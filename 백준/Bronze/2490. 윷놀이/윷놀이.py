import sys
from collections import Counter
input = sys.stdin.readline

# 각각 한 번 던진 윷짝들의 상태
states = [list(map(int, input().split())) for _ in range(3)]

# 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력
for s in states:
    # 0과 1의 개수 카운트
    counter = Counter(s)
    
    if counter[0] == 0:  # 모(E)
        print('E')
    elif counter[0] == 1:  # 도(A)
        print('A')
    elif counter[0] == 2:  # 개(B)
        print('B')
    elif counter[0] == 3:  # 걸(C)
        print('C')
    else:  # 윷(D)
        print('D')