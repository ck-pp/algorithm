def solution(absolutes, signs):
    return sum(n if sign else -n for n, sign in zip(absolutes, signs))