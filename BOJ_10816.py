# 숫자 카드2 (#10816)
# Counter 모듈 이용
import sys
from collections import Counter
N = int(sys.stdin.readline())
counter = Counter(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    print(counter[arr[i]], end=" ")