def solution(my_string):
    return ''.join(s.lower() if s.isupper() else s.upper() for s in my_string)