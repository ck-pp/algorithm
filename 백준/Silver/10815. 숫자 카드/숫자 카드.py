import sys
imput = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

sorted_cards = sorted(cards)  # 오름차순
sorted_nums = sorted(nums)  # 오름차순

res = {num:0 for num in sorted_nums}  # nums 순서대로 결과 출력
i = 0  # 카드 리스트의 인덱스

for num in sorted_nums:
    # 인덱스 초과 방지
    while i < len(sorted_cards) and sorted_cards[i] < num:
        i += 1  # 다음 카드로 이동
        
    # 현재 카드가 num과 같으면 1로 기록(기본값이 0이므로)
    if i < len(sorted_cards) and sorted_cards[i] == num:
        res[num] = 1

# nums 순서대로 결과 출력
print(*[res[n] for n in nums])