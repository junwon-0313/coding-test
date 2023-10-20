def main():
    # 입력
    global N
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))
    # 전역 변수로 사용할 리스트들
    # 좌 하 우 상
    direction = [(0,-1),(1,0),(0,1),(-1,0)]
    per = [1,1,2,2,5,7,7,10,10]
    
    # 모래양 측정
    def measure_sand(graph):
        total = 0
        for i in range(N):
            for j in range(N):
                total+=graph[i][j]
        return total
    
    # 토네이도에 날리는 모래양과 알파값
    def blow_sand(graph,start):
        # y 위치 모래들은 모조리 날아감
        alpha = graph[start[0]][start[1]]
        graph[start[0]][start[1]] =0
        sand_per = []
        # 소수점 아래 버림
        for i in per:
            sand_per.append(alpha*i//100)
        alpha -= sum(sand_per)
        sand_per.append(alpha)
        return sand_per
    
    # 토네이도
    def tornado(graph, dir, start):
        # dx, dy는 토네이도 진행방향
        dx, dy = direction[dir][0], direction[dir][1]
        x, y = start[0], start[1]
        sand_per = blow_sand(graph,(x+dx, y+dy))
        # sx, sy는 토네이도 진행방향을 기준으로 1,1,2,2,5,.. 순으로 모래가 퍼지는 곳의 x,y에 더해야하는 좌표 변화량을 정해줌
        sx = [dy, -dy, dx+2*dy, dx-2*dy,3*dx, dx+dy, dx-dy, 2*dx+dy, 2*dx-dy,2*dx]
        sy = [dx, -dx, dy+2*dx, dy-2*dx,3*dy, dy+dx, dy-dx, 2*dy+dx, 2*dy-dx, 2*dy]
        for idx in range(10):
            nx, ny = x+sx[idx], y+sy[idx]
            # 범위를 초과하면 스킵
            if 0<=nx<N and 0<=ny<N:
                graph[nx][ny]+= sand_per[idx]
        return x+dx, y+dy # 다음 토네이도의 시작점을 리턴
    
    # 초기 모래양                
    initial_sand = measure_sand(graph)
    # 바람이 같은 방향으로 이동한 거리
    change_dir = []
    for i in range(1,N):
        change_dir.append(i)
        change_dir.append(i)
    change_dir.append(N-1)
    # 초기 위치
    x, y = N//2, N//2
    # 초기 방향
    dir=0
    for i in change_dir:
        for _ in range(i):
            x,y = tornado(graph,dir, (x,y))
        dir = (dir+1)%4
    # 남아있는 모래양
    final_sand = measure_sand(graph)
    print(initial_sand-final_sand)
        
if __name__ =="__main__":
    main()