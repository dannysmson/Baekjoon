# 제로 (#10773)
from collections import deque
import sys
N = int(sys.stdin.readline())
arr = deque()
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)
tot = 0
while arr:
    tot = tot + arr.pop()
print(tot)