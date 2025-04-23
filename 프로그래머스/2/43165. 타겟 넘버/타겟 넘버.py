from collections import Counter

def solution(numbers, target):
    # dp: i-1까지 봤을 때 '합'별 경우의 수
    dp = Counter()
    dp[numbers[0]] += 1
    dp[-numbers[0]] += 1

    for num in numbers[1:]:
        # dp 자체 값을 갱신해버리면, 반복문 실행 중에 값이 바뀌어버린다.
        # 반복 도중 딕셔너리(dict)를 변경하면 RuntimeError 발생
        next_dp = Counter()
        for sum_v, cnt in dp.items():
            next_dp[sum_v + num] += cnt
            next_dp[sum_v - num] += cnt
        dp = next_dp

    return dp[target]