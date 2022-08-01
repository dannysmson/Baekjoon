import sys
def binary_search(arr, l, r, key):
    if l > r: return 0
    mid = (l + r) // 2
    if arr[mid] == key: return 1
    elif arr[mid] > key: return binary_search(arr, l, mid - 1, key)
    else: return binary_search(arr, mid + 1, r, key)
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
for i in range(M):
    print(binary_search(arr1, 0, N - 1, arr2[i]))
# 1 2 3 4 5