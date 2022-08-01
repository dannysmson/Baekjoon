# 피보나치 함수 (#1003)
# 다이나믹 프로그래밍을 이용해 피보나치 함수에 호출되는 0, 1 갯수 구하기
import sys
zero = [1, 0, 1]
one = [0, 1, 1]     
def fiboCount_zero_one(num):
    if num >= len(zero):
        for i in range(len(zero), num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num],one[num])
T = int(sys.stdin.readline())
for i in range(T):
    num = int(sys.stdin.readline())
    fiboCount_zero_one(num)