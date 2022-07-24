# 소트인사이드 (#1427)
# 정수 자릿수 내 내림차순 정렬하기
import sys
N = int(sys.stdin.readline())
arr = list()
while(True):
    if N == 0: break
    arr.append(N % 10)
    N = N // 10
arr.sort(reverse = True)
for i in range(len(arr)):
    print(arr[i], end="")