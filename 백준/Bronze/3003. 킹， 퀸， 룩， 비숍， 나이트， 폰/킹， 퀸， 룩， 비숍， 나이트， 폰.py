ans = []
data = list(map(int, input().split()))
piece = [1, 1, 2, 2, 2, 8]

for i in range(len(piece)):
    ans.append(str(piece[i]-data[i]))

print(' '.join(ans))