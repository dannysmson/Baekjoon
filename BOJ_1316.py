# 그룹 단어 체커 (#1316)
import sys
N = int(sys.stdin.readline())
cnt = 0
for i in range(N):
    str = sys.stdin.readline().rstrip()
    flag = 0
    for j in range(len(str) - 1):
        if str[j] == str[j + 1]: pass
        else:
            if str[j] in str[j+1:]:
                flag = 1
                break
    if flag == 0: cnt += 1
print(cnt)