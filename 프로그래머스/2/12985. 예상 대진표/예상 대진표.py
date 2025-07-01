import math

def solution(n,a,b):
    rounds = 1
    a_r, b_r = (a + 1) // 2, (b + 1) // 2  # A번과 B번의 게임 순서 번호
    while n > 1:
        if a_r == b_r:
            return rounds
        
        a_r = (a_r + 1) // 2
        b_r = (b_r + 1) // 2
        rounds += 1
        n //= 2