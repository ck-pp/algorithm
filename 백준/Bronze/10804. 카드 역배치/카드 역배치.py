import sys
input = sys.stdin.readline

ranges = [tuple(map(int, input().split())) for _ in range(10)]
cards = [num for num in range(1, 21)]

for a, b in ranges:
    # 인덱스와 카드 번호 헷갈리지 않도록 주의
    cards = cards[:a-1] + list(reversed(cards[a-1:b])) + cards[b:]

print(*cards)