def main():
    # 입력
    global N
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))
    # 좌 하 우 상
    direction = [(0,-1),(1,0),(0,1),(-1,0)]
    
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
        per = [1,1,2,2,5,7,7,10,10]
        sand_per = []
        for i in per:
            sand_per.append(alpha*i//100)
        alpha -= sum(sand_per)
        sand_per.append(alpha)
        return sand_per
    
    # 토네이도
    def tornado(graph, dir, start):
        dx, dy = direction[dir][0], direction[dir][1]
        x, y = start[0], start[1]
        sand_per = blow_sand(graph,(x+dx, y+dy))
        sx = [dy, -dy, dx+2*dy, dx-2*dy,3*dx, dx+dy, dx-dy, 2*dx+dy, 2*dx-dy,2*dx]
        sy = [dx, -dx, dy+2*dx, dy-2*dx,3*dy, dy+dx, dy-dx, 2*dy+dx, 2*dy-dx, 2*dy]
        for idx in range(len(sx)):
            nx, ny = x+sx[idx], y+sy[idx]
            if 0<=nx<N and 0<=ny<N:
                graph[nx][ny]+= sand_per[idx]
        return x+dx, y+dy
    
    # 초기 모래양                
    initial_sand = measure_sand(graph)
    change_dir = []
    for i in range(1,N):
        change_dir.append(i)
        change_dir.append(i)
    change_dir.append(N-1)
    x, y = N//2, N//2
    dir=0
    for i in change_dir:
        for _ in range(i):
            # 종료 조건 없어도 될 듯
            if x==0 and y==0:
                return
            x,y = tornado(graph,dir, (x,y))
        dir = (dir+1)%4
    # 마지막 모래양
    final_sand = measure_sand(graph)
    print(initial_sand-final_sand)
        
if __name__ =="__main__":
    main()