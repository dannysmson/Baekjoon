# 균형잡힌 세상 (#4949)
# 괄호 균형 확인하기
from collections import deque
import sys
while True:
    data = deque()
    str = sys.stdin.readline().rstrip()
    if str == ".": break
    flag = 0
    for ch in str:
        if ch == '(' or ch == '[':
            data.append(ch)
        elif ch == ')' or ch == ']':
            if len(data) == 0: 
                flag = 1
                break
            ch2 = data.pop()
            if (ch == ')' and ch2 == '(') or (ch == ']' and ch2 == '['): flag = 0
            else: 
                flag = 1
                break
    if flag == 0 and not data: print("yes")
    else: print("no");