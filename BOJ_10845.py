# 큐 (#10845)
import sys
def isEmpty(queue):
    if len(queue) == 0: return 1
    else: return 0
N = int(sys.stdin.readline())
queue = list()
for i in range(N):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == "push":
        queue.insert(len(queue), str[1])
    elif str[0] == "pop":
        if isEmpty(queue): print(-1)
        else:
            print(queue.pop(0))
    elif str[0] == "size":
        print(len(queue))
    elif str[0] == "empty":
        print(isEmpty(queue))
    elif str[0] == "front":
        if isEmpty(queue): print(-1)
        else: print(queue[0])
    elif str[0] == "back":
        if isEmpty(queue): print(-1)
        else: print(queue[len(queue) - 1])