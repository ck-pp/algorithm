def solution(storey):
    ans = 0
    ten = 10
    while storey > 0:
        if storey % ten > 5:
            ans += (ten - (storey%ten))
            storey = storey // ten + 1
        elif storey % ten == 5:
            ans += 5
            if (storey // ten) % ten >= 5:
                storey = (storey + 5) // ten
            else:
                storey //= ten
        else:
            ans += (storey % ten)
            storey //= ten
    return ans