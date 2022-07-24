# 1,2,3 더하기 (#9095)
import sys
N = int(sys.stdin.readline())
def cnt(num):
    if num == 1: return 1
    elif num == 2: return 2
    elif num == 3: return 4
    else: return cnt(num - 2) + cnt(num - 1) + cnt(num - 3)
for i in range(N):
    num = int(sys.stdin.readline())
    print(cnt(num))