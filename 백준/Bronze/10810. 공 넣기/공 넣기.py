import sys
input = sys.stdin.readline

N, M = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
baskets = [0] * (N + 1)

for i, j, num in infos:
    for k in range(i, j+1):
        baskets[k] = num
        
# 숫자 리스트 원소 -> 공복 구분 출력
# join은 문자열 리스트에서만 사용 가능하기 때문에 정수를 문자로 형변환 해준다.
print(' '.join(str(baskets[idx])for idx in range(1, len(baskets))))