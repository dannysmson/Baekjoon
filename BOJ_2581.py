# 소수 (#2581)
# 수의 제곱근까지만 확인하여 판별
import math
import sys
def is_prime_num(num):
    if num == 1: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
arr = list()
for num in range(M, N + 1):
    if is_prime_num(num): arr.append(num)
if len(arr) == 0: print(-1)
else:
    print(sum(arr))
    print(min(arr))