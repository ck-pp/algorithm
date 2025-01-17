import sys
input = sys.stdin.readline

problem_score = {}

# 문제 번호와 점수 맵핑하기
for i in range(1, 9):
    score = int(input())
    problem_score[i] = score
    
sorted_score = sorted(problem_score.items(), key=lambda item:-item[1])  # 점수 기준 오름차순 정렬

total_score = 0
total_problems = []
# 총점과 최종 점수에 포함되는 문제 번호 저장
for i in range(5):
    p, s = sorted_score[i]
    total_score += s
    total_problems.append(p)
    
print(total_score)
print(*sorted(total_problems))  # 오름차순 정렬 후 출력