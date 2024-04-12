def solution(cards):
    group = []
    g_idx = 0
    while g_idx < len(cards):
        box = []
        if cards[g_idx] != 0:
            idx = g_idx
            while True: # 시간복잠도 O(n^2)..
                if cards[idx] != 0:
                    box.append(cards[idx])
                    cards[idx] = 0
                    idx = box[-1] - 1
                else:
                    break
            group.append(len(box))
        else:
            g_idx += 1
    if len(group) > 1:
        group.sort()
        return group[-1] * group[-2]
    else:
        return 0