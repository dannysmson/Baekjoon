# 스택 (#10828)
import sys
N = int(sys.stdin.readline())
stk = list()
top = -1
for i in range(N):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == "push":
        top += 1
        stk.append(str[1])
    elif str[0] == "pop":
        if top == -1: print(-1)
        else: 
            print(stk.pop(top))
            top -= 1
    elif str[0] == "size": print(top + 1)
    elif str[0] == "empty": 
        if top == -1: print(1)
        else: print(0)
    elif str[0] == "top":
        if top == -1: print(-1)
        else: print(stk[top])