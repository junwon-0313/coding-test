def main():
    global N,M
    N,M = map(int,input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    score = 0
    
    def find_block(x,y, num):
        queue = [[x,y]]
        size, rainbow = 1,0
        visited[x][y]= True # 방문처리
        
        while queue:
            x,y = queue.pop(0)
            for idx in range(4):
                nx, ny = x+dx[idx], y+dy[idx]
                if nx<0 or nx>N-1 or ny<0 or ny>N-1:
                    continue
                if visited[nx][ny]:
                    continue
                if graph[nx][ny]==num:                   
                    size+=1
                    queue.append([nx,ny])
                    visited[nx][ny]=True
                elif graph[nx][ny]==0:
                    rainbow+=1
                    size+=1
                    queue.append([nx,ny])
                    visited[nx][ny]=True
        return size, rainbow
    
    def reset_rainbow():
        for x in range(N):
            for y in range(N):
                if graph[x][y]==0:
                    visited[x][y]=False
    
    def bomb_block(x,y, num):
        visited = [[False]*N for _ in range(N)]
        queue = [[x,y]]
        visited[x][y]= True # 방문처리
        while queue:
            x,y = queue.pop(0)
            graph[x][y] = -2
            for idx in range(4):
                nx, ny = x+dx[idx], y+dy[idx]
                if nx<0 or nx>N-1 or ny<0 or ny>N-1:
                    continue
                if visited[nx][ny]:
                    continue
                if graph[nx][ny]==num:                   
                    queue.append([nx,ny])
                    visited[nx][ny]=True
                elif graph[nx][ny]==0:
                    queue.append([nx,ny])
                    visited[nx][ny]=True
        return
    # 마지막 행부터 시작해서 올라가면서 처리, -1이 존재한다면 -1 위치가 맨 끝으로 변경
    def gravity():
        for x in range(N-1,-1,-1):
            for y in range(N):
                if -1<=graph[x][y]<=M:
                    continue
                # 비어있을 때만 다음을 수행
                for up in range(1,x+1):
                    nx = x-up # 올라가면서
                    if graph[nx][y]==-1: # 검정 벽돌만나면 종료
                        break
                    if graph[nx][y]==-2: # 비어있으면 계속 진행
                        continue
                    graph[x][y]= graph[nx][y] # 변경
                    graph[nx][y]=-2
                    break # 하나의 블록이 아래로 떨어지면 종료
    # 반시계 방향으로 90도 회전    
    def rotate():
        rotate_graph = [[0]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                rotate_graph[-1-y][x]=graph[x][y]
        return rotate_graph

    while True:
        # 블록 찾고 터트리고 점수 얻음
        visited = [[False]*N for _ in range(N)]
        block_lst = []
        for x in range(N):
            for y in range(N):
                if visited[x][y]:
                    continue
                if 1<=graph[x][y]<=M:
                    size, rainbow = find_block(x,y,graph[x][y])
                    reset_rainbow()
                    if size>=2:
                        block_lst.append((size, rainbow, x,y))

        if len(block_lst)==0:
            print(score)
            break
        # block_lst가 비어있다면 여기서 종료!!
        size, _, x, y = sorted(block_lst, key= lambda x:(-x[0], -x[1],-x[2],-x[3]))[0] # 조건에 맞게 정렬
        bomb_block(x,y, graph[x][y]) # 블록 폭파
        score += size**2 # 점수 더해줌
        # print('INIT')
        # for i in range(N):
        #     for j in range(N):
        #         print(graph[i][j], end = '\t')
        #     print()
        
        gravity() # 중력
        # print('First Gravity')
        # for i in range(N):
        #     for j in range(N):
        #         print(graph[i][j], end = '\t')
        #     print()
        graph = rotate() # 회전, 리턴값
        # print('ROTATE')
        # for i in range(N):
        #     for j in range(N):
        #         print(graph[i][j], end = '\t')
        #     print()
        gravity() # 중력
        # print('Second Gravity')
        # for i in range(N):
        #     for j in range(N):
        #         print(graph[i][j], end = '\t')
        #     print()
        
if __name__=='__main__':
    main()
    