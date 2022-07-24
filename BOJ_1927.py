# 최소힙 (#1927)
import sys
import heapq
N = int(sys.stdin.readline())
heap = list()
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0: 
        if len(heap) == 0: print(0)
        else: print(heapq.heappop(heap))
    else: heapq.heappush(heap, num)