# 듣보잡 (#1764)
import sys
N,M = map(int, sys.stdin.readline().rstrip().split())
str1 = set(sys.stdin.readline().rstrip() for _ in range(N))
str2 = set(sys.stdin.readline().rstrip() for _ in range(M))
arr = list()
for str in str1:
    if str in str2:
        arr.append(str)
arr.sort()
print(len(arr))
for str in arr:
    print(str)