import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

answers = []

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    L = deque()
    isLeft = True
    for e in nums:
        if isLeft:
            L.appendleft(e)
        else:
            L.append(e)
        isLeft = not isLeft
    
    maxDifference = abs(L[0] - L[1])

    for i in range(N - 1):
        maxDifference = max(abs(L[i] - L[i + 1]), maxDifference)

    answers.append(maxDifference)

print("\n".join([str(e) for e in answers]))