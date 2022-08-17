# 카드 정렬하기 (#1715)
# 그리디 알고리즘 + 자료구조(heap 모듈)
import sys
import heapq
N = int(sys.stdin.readline())
heap = [int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(heap)
tot = 0
if len(heap) == 1: print(0)
else:
    while(len(heap) >= 2):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        tot += (a + b)
        heapq.heappush(heap, a + b)
    print(tot)