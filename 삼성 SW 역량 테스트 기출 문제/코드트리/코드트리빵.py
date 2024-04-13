n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
target = [(-1,-1)]
for _ in range(m):
    x, y = map(int,input().split())
    target.append((x-1,y-1))
def print_g():
    print("@@@@@")
    for x in range(n):
        for y in range(n):
            print(graph[x][y], end = ' ')
        print()
dxs, dys = [-1,0,0,1], [0,-1,1,0] # 상 좌 우 하: 우선 순위
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_distance(start,t):
    q =[]
    q.append((start[0],start[1],0))
    visited= [[False]*n for _ in range(n)]
    visited[start[0]][start[1]]=True
    while q:
        x,y,cnt = q.pop(0)
        if (x,y)==t:
            return cnt
        for dx, dy in zip(dxs, dys):
            nx,ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]==-1:
                continue
            visited[nx][ny]=True
            q.append((nx,ny,cnt+1))
    return 10000 # 도착 못했을 때


def find_basecamp(t): # 목적지 편의점과 가까운 베이스 캠프 찾기
    temp_base = []
    for x,y in basecamp:
        if graph[x][y]==-1:
            continue
        # 못가는 것을 제외하고 거리를 체크해야함
        distance = find_distance((x,y),t)
        temp_base.append((distance, x,y))
    _,base_x,base_y = sorted(temp_base, key=lambda x:(x[0],x[1],x[2]))[0]
    return (base_x, base_y)

def find_route(k):
    q = []
    q.append((guest[k],[]))
    visited =[[False]*n for _ in range(n)]
    visited[guest[k][0]][guest[k][1]]=True
    while q:
        s, r = q.pop(0)
        x, y = s
        if (x,y) == target[k]:
            return r[0]
        for dx,dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if graph[nx][ny]==-1:
                continue
            if visited[nx][ny]:
                continue
            r.append((nx,ny))
            q.append(((nx,ny),r[:]))
            visited[nx][ny]=True
            r.pop()

basecamp = [] # 베이스 캠프 관리
for x in range(n):
    for y in range(n):
        if graph[x][y]==1:
            basecamp.append((x,y))
cnt, time=0,0 # 편의점 도착시
arrived = [False for _ in range(m+1)] # 목적지 도착
guest = [(-1,-1) for _ in range(m+1)]
while True:
    time+=1
    # print('TIME',time)
    change_lst =[]
    # 이동가능한 사람 중에서 최단 거리 찾기
    for t in range(1,min(m+1,time+1)):
        if arrived[t]: # 방문했다면
            continue
        # print('TARGET',t, target[t])
        if guest[t]!=(-1,-1):
            # guest가 원하는 편의점으로 이동할 때, 다음 좌표를 찾음
            next_pos = find_route(t)
            # 다음 좌표가 도착 편의점이라면 ->
            if next_pos== target[t]:
                arrived[t]=True
                change_lst.append(next_pos)
                cnt+=1
            else:
                guest[t] = next_pos
        if guest[t]==(-1,-1): # t==time # 손님이 입장 전이라면 가까운 베이스 캠프로 입주 후, 이동
            # 격자에 있는 사람들이 모두 없어지면 이동 불가 처리하기
            base_x, base_y = find_basecamp(target[t])
            guest[t] = (base_x,base_y)
            change_lst.append((base_x,base_y))

    for x, y in change_lst:
        graph[x][y]=-1

    # print_g()

    if cnt==m:
        print(time)
        break

