# 수들의 합 (#1789)
import sys
num = int(sys.stdin.readline().rstrip())
idx = 1
N = 0
while True:
    num -= idx
    N += 1
    idx += 1
    if idx > num: break
print(N)