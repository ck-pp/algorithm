from collections import defaultdict, Counter

def solution(weights):
    # 탐승자 무게 * 시소 축과 좌석 간 거리 곱 동일
    # 거리: 2, 3, 4
    count = 0
    weight_counts = Counter(weights)
    distance_ratios = [2/3, 2/4, 3/2, 3/4, 4/2, 4/3]
    
    # 모든 몸무게에 대한 짝꿍 수 계산
    for weight in weights:
        weight_counts[weight] -= 1  # 현재 무게를 제외
        
        # 같은 무게끼리 짝꿍 가능한 경우 (자기 자신과 같은 무게는 중복 계산 방지)
        if weight_counts[weight] > 0:
            count += weight_counts[weight]
        
        # 다른 무게끼리 짝꿍 가능한 경우
        for ratio in distance_ratios:
            target_w = weight * ratio
            if target_w in weight_counts:
                count += weight_counts[target_w]
    
    return count