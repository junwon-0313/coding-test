# 직사각형 영역의 경계에 있는 숫자들을 시계방향으로 한칸씩 shift
# 평균값: 버림
n, m, q = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

wind = []
for _ in range(q):
    r1,c1,r2,c2 = map(int, input().split())
    wind.append((r1-1,c1-1,r2-1,c2-1))

def rotate_block(r1,c1,r2,c2):
    end_c2 = graph[r1][c2]
    for nc in range(c2,c1,-1): # 상단
        graph[r1][nc] = graph[r1][nc-1]
    end_r2 = graph[r2][c2]
    for nr in range(r2,r1+1,-1):
        graph[nr][c2] = graph[nr-1][c2]
    graph[r1+1][c2] = end_c2
    end_c1 = graph[r2][c1]
    for nc in range(c1,c2-1):
        graph[r2][nc] = graph[r2][nc+1]
    graph[r2][c2-1] = end_r2
    for nr in range(r1,r2-1):
        graph[nr][c1] = graph[nr+1][c1]
    graph[r2-1][c1] = end_c1

def print_g():
    for x in range(n):
        for y in range(m):
            print(graph[x][y],end =' ')
        print()
def in_range(x,y):
    return 0<=x<n and 0<=y<m
dxs, dys = [0,1,-1,0,0], [0,0,0,1,-1]

def avg(x,y):
    temp_lst = []
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx,ny):
            temp_lst.append(graph[nx][ny])
    return sum(temp_lst)//len(temp_lst)

def avg_block(r1,c1,r2,c2):
    # 저장
    tmp_graph = [[-1]*m for _ in range(n)]
    for nr in range(r1,r2+1):
        for nc in range(c1,c2+1):
            tmp_graph[nr][nc] = avg(nr, nc)

    # 값 가져오기
    for nr in range(r1,r2+1):
        for nc in range(c1,c2+1):
            graph[nr][nc] = tmp_graph[nr][nc]

def blow():
    for r1,c1,r2,c2 in wind:
        # print_g()
        rotate_block(r1,c1,r2,c2)
        # print('rotate')
        # print_g()
        avg_block(r1,c1,r2,c2)
        # print('avg')
    print_g()

blow()
