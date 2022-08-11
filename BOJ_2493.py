# 탑 (#2493)
# 다시 풀어볼것
import sys
from collections import deque
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
queue = deque()
answer = [0 for _ in range(N)]
for i in range(N):
    while queue:
        if queue[-1][1] >= arr[i]:
            answer[i] = queue[-1][0] + 1
            break
        queue.pop()
    queue.append([i, arr[i]])
print(*answer)