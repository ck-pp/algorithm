import sys
input = sys.stdin.readline

n = int(input())
birth_infos = []
for _ in range(n):
    name, d, m, y = input().strip().split()
    d, m, y = int(d), int(m), int(y)
    
    birth_infos.append([name, d, m, y])

# 년도 -> 달 -> 일 기준 오름차순 정렬
birth_infos.sort(key=lambda info:(info[3], info[2], info[1]))

print(birth_infos[-1][0])  # 나이 가장 적은 사람 이름 출력
print(birth_infos[0][0])  # 나이 가장 많은 사람 이름 출력