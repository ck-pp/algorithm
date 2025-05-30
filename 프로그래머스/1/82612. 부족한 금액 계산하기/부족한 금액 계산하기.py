def solution(price, money, count):
    need = sum([price * i for i in range(1, count+1)])
    
    return need - money if need - money > 0 else 0