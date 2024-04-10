n,m,k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
runner = [(-1,-1)]
for _ in range(m):
    x, y =map(int,input().split())
    runner.append((x-1,y-1))
tmp = tuple(map(int,input().split()))
exit = (tmp[0]-1, tmp[1]-1) # 출구 좌표 업데이트 필요
# for idx, run in enumerate(runner):
#     if idx==0:
#         continue
#     graph[run[0]][run[1]]=-1*idx

graph[exit[0]][exit[1]]=-100 # 그래프 상에 표시
dxs, dys= [-1,1,0,0], [0,0,-1,1] # 상 하 좌 우
survive = [True for _ in range(m+1)] # 생존 여부
score = [0 for _ in range(m+1)] # 점수
died_cnt =0
def print_g(g):
    for x in range(len(g)):
        for y in range(len(g[0])):
            print(g[x][y], end = ' ')
        print()

def distance(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move_runner():
    global exit, died_cnt
    for idx, run in enumerate(runner): # 참가자 위치
        if idx==0:
            continue
        if not survive[idx]: # 생존자가 아니라면
            continue
        for dx, dy in zip(dxs,dys):
            nx,ny = run[0]+dx, run[1]+dy
            if not in_range(nx,ny):
                continue
            if graph[nx][ny]>0:
                continue
            # 상하 먼저 만족하면 동작 후 break
            # 가까워야함
            if distance(exit,(run[0],run[1]))<=distance(exit,(nx,ny)):
                continue
            runner[idx] = (nx,ny)
            score[idx]+=1
            if (nx,ny) == exit:
                survive[idx]=False
                died_cnt+=1
            break

def rotate(metrix):
    tmp_metrix = [[0]*len(metrix[0]) for _ in range(len(metrix))]
    for x in range(len(metrix)):
        for y in range(len(metrix[0])):
            tmp_metrix[y][-1-x] = metrix[x][y]
    return tmp_metrix

def rotate_maze(): # 미로가 돌아갈 떄 참가자도 돌아가야함
    global exit
    # 가장 작은 정사각형: 참가자 최소 한명 이상 + 출구 포함
    rect_lst = []
    for idx, run in enumerate(runner): # 참가자 위치
        if idx==0:
            continue
        if not survive[idx]: # 생존자가 아니라면
            continue
        dis = max(abs(run[0]-exit[0]), abs(run[1]-exit[1]))
        r, c = max(run[0], exit[0])-dis, max(run[1], exit[1])-dis
        if r<0:
            r=0
        if c<0:
            c=0
        rect_lst.append((dis, r,c))
    rect_lst.sort(key= lambda x:(x[0],x[1],x[2]))
    # print(rect_lst)
    if len(rect_lst)==0:
        return
    rect_s, rect_r, rect_c = rect_lst[0]
    # 회전
    before_rotate = []
    for r in range(rect_r, rect_r+rect_s+1):
        t = []
        for c in range(rect_c, rect_c+rect_s+1):
            t.append(graph[r][c])
        before_rotate.append(t)
    tmp_rotate = rotate(before_rotate)
    # print('@@',rect_s, rect_r, rect_c)
    # print_g(before_rotate)
    for r in range(rect_r, rect_r+rect_s+1):
        for c in range(rect_c, rect_c+rect_s+1):
            graph[r][c] = tmp_rotate[r-rect_r][c-rect_c]
            # print(tmp_rotate[r-rect_r][c-rect_c])
            # 내구도 -1
            if graph[r][c]>0:
                graph[r][c]-=1
            if graph[r][c] <0 and graph[r][c]!=-100:
                runner[-1*graph[r][c]] = (r,c)
            if graph[r][c]==-100:
                exit = (r,c)
    for idx, run in enumerate(runner): # 참가자 위치 회전
        if idx==0:
            continue
        if rect_r<=run[0]<rect_r+rect_s+1 and rect_c<=run[1]<rect_c+rect_s+1:
            # print('@@@@@CHANGE')
            # print(runner[idx])
            runner[idx] = ((run[1]-rect_c)%(rect_s+1)+rect_r, (-run[0]+rect_r-1)%(rect_s+1)+rect_c)
            # print(runner[idx])

for time in range(k): # k초마다 반복
    move_runner()
    # print("MOVE", time)
    # print_g(graph)
    rotate_maze()
    # print("ROTATE", time)
    # print_g(graph)
    if died_cnt==m:
        break

# print('@@')
print(sum(score))
print(exit[0]+1, exit[1]+1)
# metrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# print(rotate(metrix))

