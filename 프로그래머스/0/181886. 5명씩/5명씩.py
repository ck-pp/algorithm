def solution(names):
    return [names[idx] for idx in range(len(names)) if idx % 5 == 0]