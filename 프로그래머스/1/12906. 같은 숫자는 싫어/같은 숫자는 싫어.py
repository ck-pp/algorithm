def solution(arr):
    n = len(arr)
    ans = [arr[0]]  # 정답 배열 초기화
    
    for i in range(1, n):
        # 연속적으로 나타나는 값이 아닌 경우
        if arr[i-1] != arr[i]:
            ans.append(arr[i])
            
    return ans