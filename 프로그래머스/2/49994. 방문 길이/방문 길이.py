def solution(dirs):
    curr_pos = [0, 0]
    routes = set()
    for d in dirs:
        r = curr_pos.copy()
        if d == 'U' and curr_pos[1] < 5:
            curr_pos[1] += 1
        elif d == 'D' and curr_pos[1] > -5:
            curr_pos[1] -= 1
        elif d == 'R' and curr_pos[0] < 5:
            curr_pos[0] += 1
        elif d == 'L' and curr_pos[0] > -5:
            curr_pos[0] -=1
        if r != curr_pos:
            r.extend(curr_pos)
            routes.add(tuple(r))
    for ro in list(routes):
        re_r = list(ro[2:])+(list(ro[:2]))
        if tuple(re_r) in routes:
            routes.remove(ro)
    return len(routes)