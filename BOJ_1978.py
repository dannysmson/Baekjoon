#소수 찾기 (#1978)
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(N):
    cnt = 0
    for j in range(1, arr[i] + 1):
        if arr[i] % j == 0: cnt += 1
    if cnt == 2: count += 1
print(count)