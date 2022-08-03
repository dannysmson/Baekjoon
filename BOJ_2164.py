# 카드2 (#2164)
import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
queue = deque()
for i in range(1, N + 1): queue.append(i)
while True:
    if len(queue) == 1: 
        print(queue.pop())
        break
    queue.popleft()
    num = queue.popleft()
    queue.append(num)