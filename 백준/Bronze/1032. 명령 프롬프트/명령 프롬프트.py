import sys
input = sys.stdin.readline

N = int(input())
strings = []

# 입력받은 파일명 저장
for _ in range(N):
    # 문자열을 특정 값을 바꿀 수 없기 때문에 리스트로 변환해 저장한다.
    strings.append(list(input().strip()))

n = len(strings[0])  # 파일명 길이
for i in range(1, len(strings)):
    for j in range(n):
        if strings[0][j] != strings[i][j]:
            strings[0][j] = '?'

# 정답 문자열 출력
print(''.join(strings[0]))