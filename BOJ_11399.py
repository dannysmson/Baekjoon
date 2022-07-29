# ATM (#11399)
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
sum = tot = 0
for i in range(len(arr)):
    tot += arr[i]
    sum += tot
print(sum)