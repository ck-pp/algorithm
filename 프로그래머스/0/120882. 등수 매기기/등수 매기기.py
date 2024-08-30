def solution(score):
    idx_rank = [[idx, sum(s)] for idx, s in enumerate(score)]
    result = [0 for _ in range(len(score))]
    idx_rank.sort(key=lambda x : x[1], reverse=True)
    rank = duplication = 0
    
    for i in range(len(idx_rank)):
        rank += 1
        if (0 < i and idx_rank[i][1] == idx_rank[i-1][1]):
            duplication += 1
            result[idx_rank[i][0]] = rank - duplication
        else:
            duplication = 0
            result[idx_rank[i][0]] = rank 
        
    return result