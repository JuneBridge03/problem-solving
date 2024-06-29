N, S = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = 0
nowS = arr[0]

answer = N + 1

while end < N:
    if nowS >= S:
        answer = min(end - start + 1, answer)
        if start < end:
            nowS -= arr[start]
            start += 1
            continue
    
    end += 1
    if end >= N:
        break
    nowS += arr[end]

print(answer * int(answer != (N + 1)))