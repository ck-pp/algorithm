import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    one_winnings = [0, 500, 300, 200, 50, 30, 10]
    two_winnings = [0, 512, 256, 128, 64, 32]
    
    # 2회에서는 인덱스와 수상 인원이 다르기 때문에 변수를 따로 갖는다.
    idx1, idx2, people = 1, 1, 1  # 1/2회 페스티벌 인덱스, 2회 페스티벌 현재 등수 구간 인원
    while idx1 < a:
        a -= idx1
        idx1 += 1
    while people < b:
        b -= people
        idx2 += 1
        people *= 2
    
    total_winnings = 0
    total_winnings += (one_winnings[idx1] if (idx1 < len(one_winnings) and a > 0) else 0)
    total_winnings += (two_winnings[idx2] if (idx2 < len(two_winnings) and b > 0) else 0)
    
    print(total_winnings * 10000)  # 만원 단위이므로