n,m,k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
rest = [[0]*m for _ in range(n)]

def print_g():
    print('@@@@@')
    for x in range(n):
        for y in range(m):
            print(graph[x][y], end = ' ')
        print()

# 공격자 찾기
def find_attacker():
    temp_lst =[] #공격력낮음, 가장 최근 공격, 행+열, 열
    for x in range(n):
        for y in range(m):
            if graph[x][y]==0: # 부서진 포탑
                continue
            temp_lst.append((graph[x][y], rest[x][y], x+y,y))
    _,_,both,c = sorted(temp_lst, key=lambda x:(x[0],-x[1],-x[2],-x[3]))[0]
    return (both-c,c)



# 공격 대상 찾기
def find_defender(attack):
    temp_lst =[] #공격력높음, 가장 오래전 공격, 행+열, 열
    for x in range(n):
        for y in range(m):
            if graph[x][y]==0: # 부서진 포탑
                continue
            if (x,y)==attack:
                continue
            temp_lst.append((graph[x][y], rest[x][y], x+y,y))
    _,_,both,c = sorted(temp_lst, key=lambda x:(-x[0],x[1],x[2],x[3]))[0]
    return (both-c,c)


dxs, dys = [0,1,0,-1], [1,0,-1,0]
# 레이저
def lazer(attack, target): # bfs 최단 거리
    q =[]
    q.append((attack, []))
    visited = [[False]*m for _ in range(n)]
    visited[attack[0]][attack[1]]=True
    while q:
        pos, move_lst = q.pop(0)
        # print(move_lst)
        x, y = pos
        if pos == target:
            return move_lst[:]

        for dx,dy in zip(dxs, dys):
            nx, ny = (x+dx)%n, (y+dy)%m
            if graph[nx][ny]==0:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny]=True
            move_lst.append((nx,ny))
            q.append(((nx,ny),move_lst[:]))
            move_lst.pop()
    return False

def count_tower():
    cnt =0
    for x in range(n):
        for y in range(m):
            if graph[x][y]!=0:
                cnt+=1
    return cnt

# 포탄
def bomb(target, power):
    damaged =[target]
    x, y = target
    for dx, dy in zip([0,0,1,-1,1,1,-1,-1],[1,-1,0,0,1,-1,1,-1]):
        nx, ny = (x+dx)%n, (y+dy)%m
        if graph[nx][ny]==0:
            continue
        damaged.append((nx,ny))
        graph[nx][ny]=max(graph[nx][ny]-power//2,0)
    graph[x][y]=max(graph[x][y]-power,0)
    return damaged

for time in range(1,k+1):
    # print('Time',time)
    # print_g()
    attack = find_attacker()
    graph[attack[0]][attack[1]]+=(n+m)
    rest[attack[0]][attack[1]]= time
    power = graph[attack[0]][attack[1]]
    target = find_defender(attack)
    # print('attacker,', attack)
    # print('target', target)
    # 레이저
    attack_move = lazer(attack, target)
    if attack_move:
        # print('LAZER')
        for x,y in attack_move:
            if (x,y)==target:
                graph[x][y]=max(graph[x][y]-power,0)
                continue
            graph[x][y]=max(graph[x][y]-power//2,0)
        # 남아있는 포탑 +1
        for x in range(n):
            for y in range(m):
                if graph[x][y]!=0 and (x,y) not in attack_move and (x,y)!=attack:
                    graph[x][y]+=1
    else:
        # print('BOMB')
        damage_lst = bomb(target, power)
        for x in range(n):
            for y in range(m):
                if graph[x][y]!=0 and (x,y) not in damage_lst and (x,y)!=attack:
                    graph[x][y]+=1
    if count_tower()==1:
        break


ans = 0
for x in range(n):
    for y in range(m):
        ans = max(ans, graph[x][y])
print(ans)
