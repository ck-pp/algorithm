def solution(players, callings):
    name_rank = {name: idx for idx, name in enumerate(players)}
    rank_name = {idx: name for idx, name in enumerate(players)}

    for name in callings:
        front_name = rank_name[name_rank[name] - 1]
        rank_name[name_rank[name]] = front_name
        rank_name[name_rank[name] - 1] = name
        name_rank[name] -= 1
        name_rank[front_name] += 1
        
    return list(rank_name.values())