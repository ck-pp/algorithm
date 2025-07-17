def solution(d, budget):
    d.sort()  # 신청 금액별 오름차순 정렬
    
    now, total_money = 0, 0
    for money in d:  # 모든 부서에 지원 가능한 경우
        # 지원금이 예산을 넘어가기 전에 종료
        if total_money + money > budget:
            break
        total_money += money
        now += 1
    
    return now