from collections import deque

def solution(sequence, k):
    q = deque([])  # 부분 수열 담을 큐
    sum_v = 0  # 부분 수열 원소 합
    ans = []  # (부분 수열 길이, [시작idx, 끝idx])
    
    for i in range(len(sequence)):
        num = sequence[i]
        q.append(num)
        sum_v += num
            
        # 부분 수열 합이 k 이상일 경우
        if sum_v >= k:
            # 큐에 원소가 있고, 합이 k보다 클 동안 앞쪽부터 원소 제거
            while q and sum_v > k:
                sum_v -= q.popleft()
            
            # 합이 k일 경우
            if sum_v == k:
                start, end = i - len(q) + 1, i  # 시작 인덱스, 마지막 인덱스
                ans.append((end - start + 1, [start, end]))
                
                while q and sum_v > k:
                    sum_v -= q.popleft()
    
    # 1.부분 수열 길이 기준 2.시작 인덱스 기준 오름차순 정렬 
    ans.sort(key=lambda x:(x[0], x[1][0]))
    
    return ans[0][1]