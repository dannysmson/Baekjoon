# 덱 (#10866) deque 구현
import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    str = list(sys.stdin.readline().rstrip().split())
    if str[0] == "push_back":
        queue.append(str[1])
    elif str[0] == "push_front":
        queue.appendleft(str[1])
    elif str[0] == "front":
        print(queue[0])
    elif str[0] == "back":
        print(queue[len(queue) - 1])
    elif str[0] == "size":
        print(len(queue))
    elif str[0] == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif str[0] == "pop_front":
        if len(queue) == 0: print(-1)
        else: print(queue.popleft())
    elif str[0] == "pop_back":
        if len(queue) == 0: print(-1)
        else: print(queue.pop())