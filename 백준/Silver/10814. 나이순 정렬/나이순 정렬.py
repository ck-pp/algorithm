import sys
input = sys.stdin.readline

N = int(input())  # 회원수
name_ages = [(register_num, input().split()) for register_num in range(N)]  # 각 회원 (가입번호, [이름, 나이])

# 정렬 기본: 오름차순!
name_ages.sort(key=lambda x:(int(x[1][0]), x[0]))
for _, na in name_ages:
    name = na[1]
    age = na[0]
    print(age + " " + name)