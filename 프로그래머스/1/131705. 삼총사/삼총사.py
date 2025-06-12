from itertools import combinations

def solution(number):
    combination = combinations(number, 3)  # 3명의 정수 번호 조합
    
    # 3명의 정수 번호 합이 0일 경우(= 삼총사일 경우) +1
    return sum(list(1 if sum(combi) == 0 else 0 for combi in combination))