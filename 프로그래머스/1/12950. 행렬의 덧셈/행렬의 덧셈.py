def solution(arr1, arr2):
    c_l = len(arr1)  # 열 길이
    r_l = len(arr1[0])  # 행 길이
    ans = [[0] * r_l for _ in range(c_l)]
    
    for i in range(c_l):
        for j in range(r_l):
            ans[i][j] = arr1[i][j] + arr2[i][j]
    
    return ans