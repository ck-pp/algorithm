def solution(d, budget):
    d.sort()  # 신청 금액별 오름차순 정렬
    
    total_money = 0
    for i in range(len(d)):  # 모든 부서에 지원 가능한 경우
        # 지원금이 예산을 넘어가기 전에 종료
        if total_money + d[i] > budget:
            return i
        total_money += d[i]
    
    return i + 1