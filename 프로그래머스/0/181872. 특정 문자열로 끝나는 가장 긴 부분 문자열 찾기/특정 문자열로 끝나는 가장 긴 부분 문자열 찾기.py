def solution(myString, pat):
    myString = myString.replace(pat, '*')
    for i in range(len(myString) - 1, -1, -1):
        if (myString[i] == '*'):
            return myString[:i+1].replace('*', pat)
            