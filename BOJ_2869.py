# 달팽이는 올라가고 싶다 (#2869)
from math import ceil
import sys
A,B,V = map(int, sys.stdin.readline().split())
x = ceil((V - A) / (A - B) + 1)
print(x)