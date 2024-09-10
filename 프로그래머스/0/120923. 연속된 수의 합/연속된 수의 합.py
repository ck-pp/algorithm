def solution(num, total):
    res = []
    diff = 1
    if total % num > 0:  # 중간값 = total//num, total//num + 1
        stdNum1, stdNum2 = total//num, total//num + 1
        res.extend([stdNum1, stdNum2])
        while len(res) < num:
            res.extend([stdNum1 - diff, stdNum2 + diff])
            diff += 1
    else:  # 중간값 = total//num
        stdNum = total // num
        res.append(stdNum)
        while len(res) < num:
            res.extend([stdNum - diff, stdNum + diff])
            diff += 1
    return sorted(res)