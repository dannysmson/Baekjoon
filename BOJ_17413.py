# 단어 뒤집기2 (#17413)
# deque 이용
import sys
from collections import deque
def appendList(ans, queue):
    while queue:
        ans.append(queue.pop())
str = sys.stdin.readline().rstrip()
queue = deque()
ans = list()
idx = 0
while idx < len(str):
    if str[idx] == "<":
        appendList(ans, queue)
        while True:
            ans.append(str[idx])
            if str[idx] == ">": break
            idx += 1
    elif str[idx] == " ":
        appendList(ans, queue)
        ans.append(" ")
    else:
        queue.append(str[idx])
    idx += 1
appendList(ans,queue)
print("".join(ans))