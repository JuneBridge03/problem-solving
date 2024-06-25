import sys
input = sys.stdin.readline

INF = 2 ** 31 - 1

N = int(input())

matrix_sizes = []

for _ in range(N):
    r, c = map(int, input().split())
    matrix_sizes.append((r, c))

dp = [[INF for _ in range(i + 1)] for i in range(N)]

def get_min_count(start, end):
    if dp[end][start] != INF:
        return dp[end][start]
    
    if start == end:
        dp[end][start] = 0
        return 0
    
    if start + 1 == end:
        dp[end][start] = matrix_sizes[start][0] * matrix_sizes[start][1] * matrix_sizes[end][1]
        return dp[end][start]
    
    for i in range(start, end):
        dp[end][start] = min(dp[end][start], get_min_count(start, i) + get_min_count(i + 1, end) + matrix_sizes[start][0] * matrix_sizes[i][1] * matrix_sizes[end][1])
    
    return dp[end][start]

print(get_min_count(0, N - 1))