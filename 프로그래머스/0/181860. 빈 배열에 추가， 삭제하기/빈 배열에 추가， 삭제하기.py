def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i] == True:
            X.extend(arr[i] for _ in range(arr[i] * 2))
        else:
            X = X[:len(X) - arr[i]]
    return X