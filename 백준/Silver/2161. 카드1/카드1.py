import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cards = deque([i for i in range(1, N+1)])

remove_cards = []
while len(cards) > 1:
    remove_cards.append(cards.popleft())
    cards.append(cards.popleft())

print(*remove_cards, *cards)