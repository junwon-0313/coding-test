def main():
    #오, 왼, 위, 아래
    direction = [(0,1),(0,-1),(-1,0),(1,0)]

    # 온도, 온풍기 위치, 방향
    # 벽이랑 범위를 초과하지 않으면 온풍기!
    def fan(start, d, wall, visited, cnt):
        #cnt=0이면 종료
        r, c = len(temp_graph), len(temp_graph[0])
        if cnt ==0:
            return
        x, y =start[0], start[1]

        dx, dy = direction[d][0], direction[d][1]
        nx, ny = x+dx, y+dy

        # 전진 시에만
        if 0<=nx<r and 0<=ny<c:
            if tuple([(x,y), (nx,ny)]) not in wall and tuple([(nx,ny), (x,y)]) not in wall and not visited[nx][ny]:

                temp_graph[nx][ny]+=cnt
                visited[nx][ny]=True
                fan((nx,ny), d, wall, visited, cnt-1)

        # 대각선 이동
        nx2, ny2 = nx+dy, ny+dx
        if 0<=nx2<r and 0<=ny2<c:
            if tuple([(nx,ny), (nx2,ny2)]) not in wall and tuple([(nx2,ny2), (nx,ny)]) not in wall:
                fan((nx2,ny2), d, wall, visited, cnt-1)

        nx3, ny3 = nx-dy, ny-dx
        if 0<=nx3<r and 0<=ny3<c:
            if tuple([(nx,ny), (nx3,ny3)]) not in wall and tuple([(nx3,ny3), (nx,ny)]) not in wall:
                fan((nx3,ny3), d, wall, visited, cnt-1)

    # 온도 조절
    def adjust_temp(temp_graph, wall):
        # 오른쪽, 아래 방향만 서치
        dx, dy = (0,1), (1,0)
        # 임시 저장 후, 일괄 업데이트
        tmp_graph = [[0]*len(temp_graph[0]) for _ in range(len(temp_graph[0]))]
        for x in range(len(temp_graph)):
            for y in range(len(temp_graph[0])):
                for k in range(2):
                    # 오른쪽
                    nx, ny = x+dx[k], y+dy[k]
                    if nx<0 or nx>len(temp_graph)-1 or ny<0 or ny > len(temp_graph[0])-1:
                        continue
                    if tuple([(x,y), (nx,ny)]) in wall or tuple([(nx,ny), (x,y)]) in wall:
                        continue
                    if temp_graph[nx][ny]>= temp_graph[x][y]:
                        tmp_graph[nx][ny]-=(temp_graph[nx][ny]- temp_graph[x][y])//4
                        tmp_graph[x][y]+=(temp_graph[nx][ny]- temp_graph[x][y])//4
                    else:
                        tmp_graph[x][y]-=(temp_graph[x][y]- temp_graph[nx][ny])//4
                        tmp_graph[nx][ny]+=(temp_graph[x][y]- temp_graph[nx][ny])//4

        for x in range(len(temp_graph)):
            for y in range(len(temp_graph[0])):
                temp_graph[x][y] += tmp_graph[x][y]

        # 모서리 +1
        for x in (0,-1):
            for y in (0,-1):
                if temp_graph[x][y]>=1:
                    temp_graph[x][y]+=1
        # 각변 -1
        for x in (0,-1):
            for y in range(len(temp_graph[0])):
                if temp_graph[x][y]>=1:
                    temp_graph[x][y]-=1

        for x in range(len(temp_graph)):
            for y in (0,-1):
                if temp_graph[x][y]>=1:
                    temp_graph[x][y]-=1

        return temp_graph

    # 모든 범위가 넘는지 확인
    def check(temp_graph,search_lst, K):
        for i in search_lst:
            x, y = i[0], i[1]
            if temp_graph[x][y] <K:
                return False
        return True

    R,C,K = map(int, input().split())
    graph = []
    for i in range(R):
        graph.append(list(map(int,input().split())))
    W = int(input())
    # 벽
    wall = set()
    for i in range(W):
        x, y, w = (map(int,input().split()))
        if w ==0:
            wall.add(tuple([(x-1,y-1), (x-2,y-1)]))
        elif w ==1:
            wall.add(tuple([(x-1,y-1),(x-1,y)]))

    # 온도를 조사해야 하는 칸
    search_lst = []
    # 온풍기 위치와 방향
    fan_lst = []
    # 온도
    temp_graph = [[0]*C for _ in range(R)]

    # 0~R-1
    for x in range(R):
        for y in range(C):
            if graph[x][y]==0:
                continue
            elif 1<=graph[x][y]<=4:
                fan_lst.append((x,y,graph[x][y]))
            else:
                search_lst.append((x,y))

    chocolate = 0
    while True:
        # 온풍기 작동
        for idx in range(len(fan_lst)):
            x,y, dir = fan_lst[idx]
            fan((x,y), dir-1, wall, [[False]*C for _ in range(R)],5)
        # 온도 조절
        temp_graph = adjust_temp(temp_graph, wall)
        #초콜릿 먹기
        chocolate+=1
        #체크 종료 조건
        if check(temp_graph,search_lst, K):
            break
        if chocolate>100:
            chocolate=101
            break
    # print(temp_graph)
    print(chocolate)

if __name__=='__main__':
    main()


