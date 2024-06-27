T = int(input())

log = []

def get_max_dist(n):
    if n % 2 == 0:
        return (int(n / 2) + 1) * int(n / 2)
    else:
        return (int((n - 1) / 2) + 1) * int((n - 1) / 2) + int((n + 1) / 2)

for _ in range(T):
    x, y = map(int, input().split(" "))
    d = y - x
    n = 1
    while True:
        min_dist = get_max_dist(n - 1)
        max_dist = get_max_dist(n)
        if min_dist < d <= max_dist:
            log.append(str(n))
            break
        n = n + 1

print('\n'.join(log))