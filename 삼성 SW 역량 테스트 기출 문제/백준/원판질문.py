from collections import deque

n, m, t = map(int, input().split())
circle = []

for i in range(n):
    circle.append(deque(list(map(int, input().split()))))

rotateData = []

for i in range(t):
    target, direction, time = map(int, input().split())
    rotateData.append([target, direction, time])


def rotate(target, direction):
    if direction == 0:
        num = circle[target].pop()
        circle[target].appendleft(num)
    else:
        num = circle[target].popleft()
        circle[target].append(num)


# def removeNum():
#     new_circle = [deque([0]*m) for _ in range(n)]
#     flag = False
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]

#     for x in range(n):
#         for y in range(m):
#             if circle[x][y] != 0:
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]

#                     if ny == -1:
#                         ny = m - 1

#                     if ny == m:
#                         ny = 0

#                     if 0 <= nx < n:
#                         if circle[nx][ny]!=0 and circle[nx][ny] == circle[x][y]:
#                             new_circle[x][y] = 0
#                             flag = True
#                             break
#                 else:
#                     new_circle[x][y]=circle[x][y]
#     return flag, new_circle


def removeNum():
    flag = False

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for x in range(n):
        for y in range(m):
            if circle[x][y] != 0:
                
                q = deque()
                q.append([x, y, circle[x][y]])

                while q:
                    x, y, target = q.popleft()

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if ny < 0:
                            ny = m - 1

                        if ny >= m:
                            ny = 0

                        if 0 <= nx < n and circle[nx][ny] == target:
                            circle[nx][ny] = 0
                            circle[x][y] = 0
                            q.append([nx, ny, target])
                            flag = True
    return flag, circle

def adjust():
    hap = 0
    division = 0

    for x in range(n):
        for y in range(m):
            if circle[x][y] != 0:
                hap += circle[x][y]
                division += 1

    if division == 0:
        return
    average = hap / division

    for x in range(n):
        for y in range(m):
            if circle[x][y] == 0:
                continue
            if circle[x][y] > average:
                circle[x][y] -= 1
            elif circle[x][y] < average:
                circle[x][y] += 1

def rotateTarget(target, direction, time):
    for i in range(n):
        if (i + 1) % target == 0:
            for _ in range(time):
                rotate(i, direction)

# 동작
for target, direction, time in rotateData:
    # 회전
    rotateTarget(target, direction, time)
    # 터트리기 or 값 조정
    flag,circle = removeNum()
    if not flag:
        adjust()

# 출력
answer = 0
for i in range(n):
    for j in range(m):
        answer += circle[i][j]
print(answer)
