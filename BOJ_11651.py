# 좌표 정렬하기2 (#11651)
# 좌표를 y좌표가 증가하는 순으로, x좌표가 증가하는 순으로 정렬
import sys
N = int(sys.stdin.readline())
arr = list()
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda arr : (arr[1], arr[0]))
for i in range(N):
    print("%d %d" %(arr[i][0], arr[i][1]))