import sys
input = sys.stdin.readline

# x + 3y = -1 -> ax + by = c
# 4x + y = 7 -> dx + ey = f
a, b, c, d, e, f = map(int, input().split())

# 행렬식 사용(행렬의 곱)
# det != 0: 유일한 해(x, y) 가짐. det == 0: 해가 없거나 무수히 많은 해 가짐.
det = a*e - b*d

# 문제에서 유일한 해 가진다고 했으므로 det != 0 보장됨.
x = (c*e - b*f) // det
y = (a*f - c*d) // det

print(x, y)