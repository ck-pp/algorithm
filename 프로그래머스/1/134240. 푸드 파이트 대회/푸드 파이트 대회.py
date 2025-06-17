def solution(food):
    half = ''
    for i in range(1, len(food)):
        half += str(i) * (food[i] // 2)

    return half + '0' + half[::-1]