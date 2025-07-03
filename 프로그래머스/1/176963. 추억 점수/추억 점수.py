def solution(name, yearning, photo):
    # {이름: 그리움 점수}
    name_yearning = {name[i]:yearning[i] for i in range(len(name))}
    ans = []
    
    for p in photo:
        sum = 0
        for n in p:  # p: 각 사진에 찍힌 인물의 이름 배열
            if n in name_yearning:  # 그리움 점수가 존재하는 사람의 이름일 경우
                sum += name_yearning[n]
        
        ans.append(sum)
        
    return ans