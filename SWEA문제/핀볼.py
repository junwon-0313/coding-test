T = int(input())

for t in range(1,T+1):
    dxs, dys =[-1,1,0,0], [0,0,-1,1] # 상 하 좌 우
    # 블록 1~ 만나면 반환
    block =[[],
            [1,3,0,2],
            [3,0,1,2],
            [2,0,3,1],
            [1,2,3,0],
            [1,0,3,2],
            [],
            [],
            [],
            [],
            []]
    def in_range(x,y):
        return 0<=x<n and 0<=y<n

    n = int(input())
    game = []
    for _ in range(n):
        game.append(list(map(int,input().split())))
    def find_hole():
        for x in range(n):
            for y in range(n):
                if 6<=game[x][y]<=10:
                    block[game[x][y]].append((x,y))
    find_hole()

    def play_game(start, d): # 핀볼 위치와 방향
        x, y = start
        score = 0
        while True:
            nx, ny = x+dxs[d], y+dys[d]
            if not in_range(nx,ny): # 다음 좌표가 벽이면 해당 위치에 고정+ 방향만 바꾸기
                x,y, d = nx,ny, block[5][d]
                score+=1
            elif 1<=game[nx][ny]<=5:# 벽이 아니라면 좌표 갱신+ 점수 갱신 후, 방향 바꿔서 이동
                x,y, d = nx,ny, block[game[nx][ny]][d]
                score+=1
            elif 6<= game[nx][ny]<=10:# 웜홀이라면 좌표를 바꿈
                for new_x, new_y in block[game[nx][ny]]:
                    if (new_x,new_y)!=(nx,ny):
                        x,y = new_x, new_y
            else: # 블럭을 안만난다면 그냥 진행
                x, y = nx,ny
            # 종료 조건: 핀볼이 블랙 홀 or 출발 장소
            if in_range(x,y):
                if (x,y) == start or game[x][y]==-1:
                    break
        return score

    max_score = 0
    for x in range(n):
        for y in range(n):
            if game[x][y]==0:
                for d in range(4):
                    temp_score = play_game((x,y),d)
                    max_score = max(temp_score, max_score)
    print(f'#{t}',max_score)
