# 설탕 배달 (#2839)
import sys
N = int(sys.stdin.readline())
idx = N // 5
cnt = flag = 0
for i in range(idx, -1, -1):
    M = N
    cnt = i
    M = (M - 5 * i)
    if M % 3 == 0:
        cnt = cnt + M // 3
        flag = 1
        break
if flag == 0: print(-1)
else: print(cnt)