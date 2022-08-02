# 동전0 (#11047)
# 그리디 알고리즘
import sys
N,K = map(int,sys.stdin.readline().rstrip().split())
arr = list()
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
cnt = 0
arr.reverse()
for num in arr:
    cnt = cnt + K // num
    K = K % num
print(cnt)