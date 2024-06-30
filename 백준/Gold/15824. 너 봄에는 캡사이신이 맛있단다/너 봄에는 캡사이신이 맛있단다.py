N = int(input())

if N == 1:
    print(0)
    exit(0)

arr = list(map(int, input().split()))

arr.sort()

if N == 2:
    print((arr[1] - arr[0]) % 1000000007)
    exit(0)

s = 0
for i in range(len(arr) - 1):
    s += (arr[i + 1] - arr[i]) * (2 ** (i + 1) - 1) * (2 ** (N - i - 1) - 1)

print(s % 1000000007)