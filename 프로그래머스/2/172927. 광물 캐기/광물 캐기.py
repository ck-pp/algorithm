from collections import Counter

def consumed_fatigue(mineral_block):
    cnt_d = Counter(mineral_block)
    pick_case = [0, 0, 0]
    pick_case[0] = cnt_d['diamond'] + cnt_d['iron'] + cnt_d['stone']
    pick_case[1] = 5 * cnt_d['diamond'] + cnt_d['iron'] + cnt_d['stone']
    pick_case[2] = 25 * cnt_d['diamond'] + 5 * cnt_d['iron'] + cnt_d['stone']
    return pick_case
        
# 0: dia / 1: iron / 2: stone
def solution(picks, minerals):
    ans = 0
    div_m = []
    case_n = []
    sum_p = sum(picks)
    
    # minerals를 5개씩 묶어서 div_m에 저장
    for s in range(0, len(minerals), 5):
        div_m.append(minerals[s:s+5])
        case_n.append(consumed_fatigue(div_m[-1])) 
        if len(div_m) >= sum_p:
            break
        
    # 피로도가 높은 순서대로 정렬
    case_n.sort(key=lambda x: (x[2], x[1], x[0]), reverse=True)
        
    for pick_case in case_n:
        for i in range(3):
            if picks[i] > 0:
                ans += pick_case[i]
                picks[i] -= 1
                break
    
    return ans