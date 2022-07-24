# 절댓값 힙 (#11286)
import sys
import heapq
N = int(sys.stdin.readline())
heap = list()
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0: print(0)
        else: 
            arr = heapq.heappop(heap)
            print(arr[0] * arr[1])
    else:
        if num < 0: heapq.heappush(heap, (num * -1, -1))
        else: heapq.heappush(heap, (num, 1))