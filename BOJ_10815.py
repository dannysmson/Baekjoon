# 숫자 카드 (#10815)
# set 이용
import sys
N = int(sys.stdin.readline())
arr1 = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
for num in arr2:
    if num in arr1: print(1, end=" ")
    else: print(0, end=" ")