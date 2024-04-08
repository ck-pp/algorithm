def solution(phone_book):
    dict = {name:len(name) for name in phone_book}
    dict = sorted(dict.items())
    for i in range(len(dict)-1):
        if dict[i][0] == dict[i+1][0][:dict[i][1]]:
            return False
    return True