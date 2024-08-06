def solution(bandage, health, attacks):
    # 기술 시전 시간([시전 시간, 초당 회복량, 추가 회복량]) / 최대 체력 / [공격 시간, 피해량]
    cur_health = health
    success = 0
    attacks_dict = {time: mount for time, mount in attacks}
    for t in range(1, attacks[-1][0] + 1):
        if (t in attacks_dict.keys()): # 공격 당하는 타임
            success = 0
            cur_health -= attacks_dict[t]
            attacks_dict.pop(t)
            if (cur_health <= 0):
                return -1
        else: # 공격 안받는 타임
            success += 1
            cur_health += bandage[1]
            if (success == bandage[0]): # 연속 성공이 붕대 감기 시전 시간에 도달한 경우
                success = 0
                cur_health += bandage[2]
            if (cur_health > health):
                cur_health = health
    return cur_health