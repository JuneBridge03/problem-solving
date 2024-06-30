import sys
from collections import deque
input = sys.stdin.readline

DIVISOR = 1000000007

N = int(input())
arr = list(map(int, input().split()))


if N == 1:
    print(0)
    exit(0)

if N == 2:
    print(abs(arr[1] - arr[0]) % DIVISOR)
    exit(0)

arr.sort()

twoMuls = []
e = 2
for _ in range(N - 1):
    twoMuls.append(e - 1)
    e = (e * 2) % DIVISOR


s = 0
for i in range(N - 1):
    s += ((arr[i + 1] - arr[i]) * twoMuls[i] * twoMuls[N - 2 - i]) % DIVISOR

print(s % DIVISOR)