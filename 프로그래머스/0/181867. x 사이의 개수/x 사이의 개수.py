def solution(myString):
    split_string = myString.split('x')
    return [len(s) for s in split_string]