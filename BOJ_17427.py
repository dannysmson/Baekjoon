# 약수의 합2 (#17427)

import sys
N = int(sys.stdin.readline())
tot = 0
for i in range(1, N + 1):
    tot += N//i * i
print(tot)