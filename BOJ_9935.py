# 문자열 폭발 (#9935)
import sys
str = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip())
ans = list()
for ch in str:
    ans.append(ch)
    if ans[-len(bomb):] == bomb:
        ans[-len(bomb):] = []
if len(ans) == 0:
    print("FRULA")
else: print("".join(ans))