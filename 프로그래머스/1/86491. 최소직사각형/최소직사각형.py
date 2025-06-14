def solution(sizes):
    len1, len2 = -1, -1
    for w, h in sizes:
        len1 = max(len1, max(w, h))
        len2 = max(len2, min(w, h))
        
    return len1 * len2
            