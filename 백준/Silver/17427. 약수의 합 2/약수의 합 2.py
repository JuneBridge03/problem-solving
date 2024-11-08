N = int(input())

answer = 0
for i in range(1, N + 1):
    now = (N // i) * i
    answer += now
    if now == 1:
        answer += (N - i)
        break

print(answer)
