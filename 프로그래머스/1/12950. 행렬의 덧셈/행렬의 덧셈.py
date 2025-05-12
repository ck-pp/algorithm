def solution(arr1, arr2):
    rows = len(arr1)  # 행 길이
    cols = len(arr1[0])  # 열 길이
    for i in range(rows):
        for j in range(cols):
            arr2[i][j] += arr1[i][j]
    
    return arr2