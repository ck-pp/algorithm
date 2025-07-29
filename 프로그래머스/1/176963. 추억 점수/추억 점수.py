def solution(name, yearning, photo):
    ans = []
    name_idx = {name[i]:i for i in range(len(name))}
    
    for p in photo:
        sum = 0
        for j in range(len(p)):
            if p[j] in name:  # 그리움 점수가 존재하는 사람의 이름일 경우
                sum += yearning[name_idx[p[j]]]
        
        ans.append(sum)
        
    return ans