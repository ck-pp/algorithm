def solution(array, height):
    array.append(height)
    return sorted(array, reverse=True).index(height)