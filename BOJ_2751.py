import sys
import heapq
# 수 정렬하기2 (#2751)
# 힙 정렬 heapq 모듈 사용
# O(NlogN)
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
while heap:
    print(heapq.heappop(heap))