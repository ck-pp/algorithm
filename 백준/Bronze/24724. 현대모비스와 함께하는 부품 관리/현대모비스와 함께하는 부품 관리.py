import sys
input = sys.stdin.readline

T = int(input())  # 부품 관리 횟수

x = 1
for _ in range(T):
    N = int(input())  # 부품의 개수
    A, B = map(int, input().split())  # 각 그룹의 크기 제한, 무게 제한
    u_v_lists = list(map(int, input().split()) for _ in range(N))  # 각 부품의 크기와 부품에 대한 정보
    
    print("Material Management " + str(x))
    print("Classification ---- End!")
    x += 1