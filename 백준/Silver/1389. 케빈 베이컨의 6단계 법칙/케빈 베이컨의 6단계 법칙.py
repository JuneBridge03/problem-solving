from collections import deque

N, M = map(int, input().split())

network_for_cpu = [[] for _ in range(N + 1)] # 개개인에 따른 관계망 구축

for _ in range(M): # 관계망 확실하게 만들기
    e1, e2 = map(int, input().split())
    network_for_cpu[e1].append(e2)
    network_for_cpu[e2].append(e1)

answer = -1
answerKevin = N ** 2

for i in range(1, N + 1):
    kevinCnt = 0
    visited = [False] * (N + 1)
    q = deque()
    q.appendleft((i, 0))
    visited[i] = True
    while q:
        e, nowKevin = q.pop()
        kevinCnt += nowKevin
        for v in network_for_cpu[e]:
            if visited[v]:
                continue
            q.appendleft((v, nowKevin + 1))
            visited[v] = True
    
    if kevinCnt < answerKevin:
        answer = i
        answerKevin = kevinCnt

print(answer)
