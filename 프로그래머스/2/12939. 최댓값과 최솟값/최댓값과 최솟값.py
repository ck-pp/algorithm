def solution(s):
    # 공백 기준으로 숫자 저장
    nums = list(map(int, s.split()))
    min_num = str(min(nums))  # 최소값
    max_num = str(max(nums))  # 최대값
    
    return min_num + ' ' + max_num