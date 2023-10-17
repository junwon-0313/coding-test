def main(graph, N, M, K):

    # 동서남북 방향으로
    def rolling_dice(dice, direction):
        new_dice = [[0]*3 for _ in range(4)]
        if direction =='동':
            new_dice[0][1]=dice[0][1]
            new_dice[1][0]=dice[3][1]
            new_dice[1][1]=dice[1][0]
            new_dice[1][2]=dice[1][1]
            new_dice[2][1]=dice[2][1]
            new_dice[3][1]=dice[1][2]
        elif direction =='서':
            new_dice[0][1]=dice[0][1]
            new_dice[1][0]=dice[1][1]
            new_dice[1][1]=dice[1][2]
            new_dice[1][2]=dice[3][1]
            new_dice[2][1]=dice[2][1]
            new_dice[3][1]=dice[1][0]
        elif direction =='남':
            new_dice[0][1]=dice[3][1]
            new_dice[1][0]=dice[1][0]
            new_dice[1][1]=dice[0][1]
            new_dice[1][2]=dice[1][2]
            new_dice[2][1]=dice[1][1]
            new_dice[3][1]=dice[2][1]
        elif direction =='북':
            new_dice[0][1]=dice[1][1]
            new_dice[1][0]=dice[1][0]
            new_dice[1][1]=dice[2][1]
            new_dice[1][2]=dice[1][2]
            new_dice[2][1]=dice[3][1]
            new_dice[3][1]=dice[0][1]
        bottom_num = 7-new_dice[1][1]
        return new_dice, bottom_num

    #새로운 점수 표 구하기
    def score_bfs(graph, start, visited):
        dx, dy = [0,0,-1,1], [-1,1,0,0]
        queue=[]
        pos_lst = []
        pos_num = graph[start[0]][start[1]]
        queue.append(start)
        visited[start[0]][start[1]]=True
        while queue:
            s = queue.pop(0)
            x,y = s[0], s[1]
            pos_lst.append((x,y))
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or nx>N-1 or ny<0 or ny>M-1:
                    continue
                if visited[nx][ny]:
                    continue
                if graph[x][y] ==graph[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
        return pos_lst, pos_num

    global x,y
    x,y =0,0
    dir_num =0
    dice = [[0,2,0],[4,1,3],[0,5,0],[0,6,0]]
    dir_lst = ['동','남','서','북']
    dir_pos = [(0,1),(1,0),(0,-1),(-1,0)]
    result = 0
    score = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                pos_lst, pos_num = score_bfs(graph, (i,j), visited)
                for k in pos_lst:
                    score[k[0]][k[1]] = pos_num*len(pos_lst)
    # 전개도 확인
    # for i in dir_lst:
    #     print(rolling_dice(dice,i))

    # 방향 검증
    # for i in range(-4,3):
    #     print(dir_lst[i], dir_lst[(i)%4])
    #     print(dir_lst[(i-2)%4], dir_lst[(i+2)%4])

    for iter_num in range(K):
        # 굴러갈 수 있는 지 확인, 범위를 넘어간다면 방향바꾸기
        # print('###',iter_num)
        nx, ny =x + dir_pos[dir_num][0], y+dir_pos[dir_num][1]
        if nx<0 or nx>N-1 or ny<0 or ny>M-1:
            # print('Change!')
            dir_num = (dir_num+2)%4
        x, y =x + dir_pos[dir_num][0], y+dir_pos[dir_num][1]
        # print(dir_lst[dir_num],nx,ny)
        #굴러감
        dice, bottom_num= rolling_dice(dice,dir_lst[dir_num])
        # nx,ny위치에서의 점수 획득
        result+=score[x][y]
        #아랫면과 비교해 방향 결정
        if bottom_num >graph[x][y]:
            dir_num = (dir_num+1)%4
        elif bottom_num <graph[x][y]:
            dir_num = (dir_num-1)%4
        else:
            pass
    print(result)

if __name__=='__main__':
    N,M,K = map(int,input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))
    main(graph,N,M,K)
