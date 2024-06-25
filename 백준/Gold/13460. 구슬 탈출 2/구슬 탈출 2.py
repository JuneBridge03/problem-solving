
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

DOWN = 0
UP = 1
RIGHT = 2
LEFT = 3

NOTHING = '.'
WALL = '#'
HOLE = 'O'
RED = 'R'
BLUE = 'B'

N, M = map(int, input().split())

hole_pos = [-1, -1]
red_pos = [-1, -1]
blue_pos = [-1, -1]

# maps의 위치들에 대한 움직임 최솟값을 갱신해준다. 이때, 중간이나 나중에 파란색이 포함되는 경우는 "배제" 한다.
maps = [list(input()) for _ in range(N)]

for x in range(N):
    for y in range(M):
        if maps[x][y] == HOLE:
            hole_pos[0] = x
            hole_pos[1] = y
        elif maps[x][y] == RED:
            red_pos[0] = x
            red_pos[1] = y
        elif maps[x][y] == BLUE:
            blue_pos[0] = x
            blue_pos[1] = y

answer = 11

def is_red_first(rx, ry, bx, by, direction):
    if direction == DOWN or direction == UP:
        if ry != by:
            return True
        return (rx > bx) == (direction == DOWN)
    
    if rx != bx:
        return True
    return (ry > by) == (direction == RIGHT)


def move(rx, ry, bx, by, cnt = 0): # cnt는 "이전까지" 움직인 횟수
    global answer
    if cnt >= 10:
        return
    
    cnt += 1 # 이제 움직임을 추가한다.

    for DIRECTION in range(4):
        IS_RED_STOP = False
        IS_BLUE_STOP = False
        IS_RED_IN_HOLE = False
        IS_BLUE_IN_HOLE = False

        rnx = rx
        rny = ry
        bnx = bx
        bny = by

        IS_RED_FIRST = is_red_first(rx, ry, bx, by, DIRECTION)
        
        while not (IS_RED_STOP and IS_BLUE_STOP):
            if IS_RED_FIRST:
                if not IS_RED_STOP:
                    rnx += dx[DIRECTION]
                    rny += dy[DIRECTION]

                    if not (0 <= rnx < N and 0 <= rny < M) or maps[rnx][rny] == WALL:
                        rnx -= dx[DIRECTION]
                        rny -= dy[DIRECTION]
                        IS_RED_STOP = True
                    
                if not IS_BLUE_STOP:
                    bnx += dx[DIRECTION]
                    bny += dy[DIRECTION]

                    if not (0 <= bnx < N and 0 <= bny < M) or maps[bnx][bny] == WALL or (bnx == rnx and bny == rny and not IS_RED_IN_HOLE):
                        bnx -= dx[DIRECTION]
                        bny -= dy[DIRECTION]
                        IS_BLUE_STOP = True

            else:
                if not IS_BLUE_STOP:
                    bnx += dx[DIRECTION]
                    bny += dy[DIRECTION]

                    if not (0 <= bnx < N and 0 <= bny < M) or maps[bnx][bny] == WALL:
                        bnx -= dx[DIRECTION]
                        bny -= dy[DIRECTION]
                        IS_BLUE_STOP = True

                if not IS_RED_STOP:
                    rnx += dx[DIRECTION]
                    rny += dy[DIRECTION]

                    if not (0 <= rnx < N and 0 <= rny < M) or maps[rnx][rny] == WALL or (bnx == rnx and bny == rny and not IS_BLUE_IN_HOLE):
                        rnx -= dx[DIRECTION]
                        rny -= dy[DIRECTION]
                        IS_RED_STOP = True
            
            if not IS_RED_STOP and maps[rnx][rny] == HOLE:
                IS_RED_IN_HOLE = True
                IS_RED_STOP = True
                
            if not IS_BLUE_STOP and maps[bnx][bny] == HOLE:
                IS_BLUE_IN_HOLE = True
                IS_BLUE_STOP = True
        
        if IS_BLUE_IN_HOLE:
            continue

        if IS_RED_IN_HOLE:
            answer = min(answer, cnt)
            break

        if rnx == rx and rny == ry and bnx == bx and bny == by:
            continue # 의미없는 행동.

        move(rnx, rny, bnx, bny, cnt)


move(red_pos[0], red_pos[1], blue_pos[0], blue_pos[1])

if answer == 11:
    print(-1)
else:
    print(answer)