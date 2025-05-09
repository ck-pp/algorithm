def solution(s):
    remove = 0  # 제거된 모든 0의 개수
    convert = 0  # 이진 변환 횟수
    while s != '1':
        # 0의 개수
        remove += s.count('0')
        
        # 1의 개수를 이진 변환
        s = bin(s.count('1'))[2:]
        convert += 1

    return [convert, remove]
        