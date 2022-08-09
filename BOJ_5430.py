# AC (#5430)
import sys
from collections import deque
T = int(sys.stdin.readline()) #연산의 갯수
for _ in range(T):
    str = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    rev_cnt = 0
    err = True
    for ch in str:
        if ch == "R":
            rev_cnt += 1
        elif ch == "D":
            if len(queue) == 0 or N == 0:
                print("error")
                err = False
                break
            else:
                if rev_cnt % 2 ==0: queue.popleft()
                else: queue.pop()
    if err:         # reverse 갯수를 저장후 마지막에 reverse 여부 결정 (실행복잡도 이유)
        if rev_cnt % 2 != 0: queue.reverse()
        print("[" + ",".join(queue) + "]")