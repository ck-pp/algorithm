def solution(video_len, pos, op_start, op_end, commands):
    # 10초 전("prev"), 10초 후("next"), 오프닝 건너뛰기(op_start<=현재<=op_end)
    second = int(pos[:2]) * 60 + int(pos[3:])
    video_sec = int(video_len[:2]) * 60 + int(video_len[3:]) 
    s_sec = int(op_start[:2]) * 60 + int(op_start[3:])
    e_sec = int(op_end[:2]) * 60 + int(op_end[3:])
    
    if s_sec <= second <= e_sec:
            second = e_sec
            
    for cmd in commands:
        if cmd == "prev":
            second -= 10
        elif cmd == "next":
            second += 10
            
        if second < 0:
            second = 0
        if second > video_sec:
            second = video_sec
        if s_sec <= second <= e_sec:
            second = e_sec
            
    return format(second // 60, '02') + ':' + format(second % 60, '02')