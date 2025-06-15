def solution(numbers):
    ans = set()  # 중복 값 제거
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            ans.add(numbers[i] + numbers[j])
    
    return sorted(ans)  # 오름차순 정렬