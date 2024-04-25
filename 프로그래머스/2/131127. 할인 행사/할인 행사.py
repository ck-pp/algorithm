def solution(want, number, discount):
    ans = 0
    want_n = {name:num for name, num in zip(want, number)}
    for i in range(len(discount)-9):
        sales = discount[i:i+10]
        for j in want_n.keys():
            if sales.count(j) != want_n[j]:
                ans += 1
                break
    return (len(discount)-9) - ans