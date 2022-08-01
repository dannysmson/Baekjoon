# 요세푸스 문제 0 (#11866)
# deque 모듈 활용
from collections import deque
import sys
N,K = map(int, sys.stdin.readline().split())
que = deque()
for i in range(N):
    que.append(i + 1)
print("<", end = "")
while que:
    for i in range(K - 1):
        que.append(que.popleft())
    if len(que) == 1: print(que.popleft(), end = ">")
    else: print(que.popleft(), end = ", ")