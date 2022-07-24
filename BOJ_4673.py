# 셀프넘버 (#4673)
# 10000이하의 셀프넘버 출력
def self_num(N):
     for i in range(N):
        num = 0
        tmp = i
        while tmp > 0:
            num += tmp % 10
            tmp = tmp // 10
        if (num + i) == N: return 0
     return 1

for i in range(1, 10001):
    if self_num(i): print(i) 