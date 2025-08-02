def solution(n, arr1, arr2):
    # 벽 벽 = 벽, 공백 공백 = 공백, 벽 공백 또는 공백 벽 = 벽 (OR 비트 연산)
    xor_res = []
    for i in range(n):
        # OR 연산 후 이진 변환 (길이 n에 맞추기 위해 앞에 0을 채워준다.)
        xor_res.append(bin(arr1[i]|arr2[i])[2:].zfill(n))
    
    for i in range(len(xor_res)):
        xor_res[i] = xor_res[i].replace('0', ' ').replace('1', '#')

    return xor_res