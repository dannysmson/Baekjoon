# 문자열 집합 (#14425)
import sys
N, M = map(int, sys.stdin.readline().split())
s = set()
for i in range(N):
    s.add(sys.stdin.readline().rstrip())
cnt = 0
for i in range(M):
    str = sys.stdin.readline().rstrip()
    if str in s: cnt += 1
print(cnt)