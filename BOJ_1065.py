# 한수 (#1065)
def check(num):
    arr = list()
    arr = list(str(num))
    if len(arr) <= 2: return 1
    flag = 1
    for i in range(1, len(arr) - 1):
        if (int(arr[i]) - int(arr[i - 1])) != (int(arr[i + 1]) - int(arr[i])): flag = 0
    return flag
cnt = 0
N = int(input())
for i in range(1, N + 1):
    cnt += check(i)
print(cnt)