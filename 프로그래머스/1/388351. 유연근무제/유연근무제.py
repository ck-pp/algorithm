def solution(schedules, timelogs, startday):
    n = len(schedules)  # 직원 수
    ans = n  # 리턴값 초기화
    for i in range(n):
        day = startday  # 요일 체크하기 위한 변수
        # 출근 인정 시각(+10분이 정각 넘어가는 경우 고려. 855 + 10 = 865 = 905)
        schedules[i] += 10
        hour = schedules[i] // 100 + (schedules[i] % 100 // 60)
        minute = schedules[i] % 100 % 60
        possible_time = 100 * hour + minute
        
        for j in range(7):
            # 평일이고 출근 희망 시간(+10)까지 출근하지 못한 경우
            if (day - 1) % 7 < 5 and timelogs[i][j] > possible_time:
                ans -= 1  # 지각한 직원 제외
                break
            
            day += 1  # 하루 지남
    
    return ans