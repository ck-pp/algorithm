import math

def solution(n,a,b):
    rounds = 1
    a_round, b_round = (a + 1) // 2, (b + 1) // 2
    
    while n > 1:  # 게임 끝
        if a_round == b_round:
            return rounds
        
        a_round = (a_round + 1) // 2
        b_round = (b_round + 1) // 2
        rounds += 1
        n //= 2