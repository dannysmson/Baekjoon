# 단어 정렬 (#1181)
# 길이가 짧은 것 우선
# 길이가 같으면 사전 순
import sys
N = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(N)]
arr = sorted(set(arr))
arr.sort(key = lambda arr : len(arr))
for i in range(len(arr)):
    print("%s" %(arr[i]))