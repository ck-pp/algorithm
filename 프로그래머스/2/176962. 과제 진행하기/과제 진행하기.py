def solution(plans):
    # 시간 변환 함수
    def time_to_minutes(time):
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes
    
    plans.sort(key=lambda x: time_to_minutes(x[1]))

    completed = []  # 완료된 과제
    st = []  # 멈춘 과제 저장할 스택(과목, 남은 시간)
    cur_time = 0  # 현재 시각

    for plan in plans:
        name, start, duration = plan
        start_time = time_to_minutes(start)
        duration = int(duration)
        
        # 진행 중인 과제가 있는 경우, 시작 시각 이전에 끝낼 수 있는지 확인
        while st and cur_time < start_time:
            task_name, remaining_time = st.pop()
            if cur_time + remaining_time <= start_time:
                # 남은 시간을 다 사용하여 과제를 끝낼 수 있는 경우
                cur_time += remaining_time
                completed.append(task_name)
            else:
                # 남은 시간을 다 사용해도 끝내지 못하는 경우
                st.append((task_name, remaining_time - (start_time - cur_time)))
                break
        
        cur_time = start_time
        
        # 현재 과제 진행
        st.append((name, duration))

    # 모든 과제가 시작된 후 남은 과제들 처리
    while st:
        task_name, remaining_time = st.pop()
        completed.append(task_name)
    
    return completed