# 크로아티아 알파벳 (#2941)
# 크로아티아 알파벳 갯수 새기
import sys
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
str = sys.stdin.readline().rstrip()
for ch in croatia:
    str = str.replace(ch, '*')
print(len(str))