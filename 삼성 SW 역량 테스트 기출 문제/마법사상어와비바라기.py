def main():
    # 구름은 각 원소가 좌표인 리스트로 전달
    def move_rain(graph, cloud, d, s,N):
        move_cloud = []
        direction = [(0,0), (0,-1), (-1,-1), (-1,0), (-1, 1), (0, 1), (1, 1), (1,0), (1,-1)]
        for i in cloud:
            x,y = i[0], i[1]
            nx, ny = (x+s*direction[d][0])%N,(y+s*direction[d][1])%N
            graph[nx][ny]+=1
            move_cloud.append((nx,ny))
        return graph, move_cloud
    def copy_water(graph, cloud, N):
        dx, dy = [-1,-1,1,1], [-1,1,1,-1]
        for i in cloud:
            #물이 증가한 칸
            x, y = i[0], i[1]
            for j in range(4):
                nx, ny = x+ dx[j], y+dy[j]
                if nx<0 or nx>N-1 or ny<0 or ny>N-1:
                    continue
                if graph[nx][ny]>0:
                    graph[x][y]+=1
        return graph
    def make_cloud(graph, cloud):
        new_cloud = []
        for x in range(N):
            for y in range(N):
                # 모든 순간마다 cloud를 검사하면 시간초과남
                # in 연산자는 시간이 O(K) 만큼 걸리니 조심!
                if graph[x][y]>=2:
                    new_cloud.append((x,y))
        # 차집합으로 겹치지 않는 좌표만 구해서 구름만들기
        new_cloud = list(set(new_cloud) - set(cloud))
        for i in new_cloud:
            graph[i[0]][i[1]]-=2
        return graph, new_cloud

    N, M = map(int, input().split())
    # 저장된 물의 양
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))
    move_lst = []
    for i in range(M):
        move_lst.append(list(map(int,input().split())))

    # 첫번째 구름 위치는 정해짐
    cloud = [(N-1,0), (N-2,1), (N-2,0), (N-1,1)]

    for m in move_lst:
        # 구름 이동 후 비 내림, 구름 사라진 위치 저장
        graph, prev_cloud= move_rain(graph, cloud, m[0], m[1], N)
        # 대각선에 물이 있을 때, 증가
        graph = copy_water(graph, prev_cloud, N)
        # 구름 생성
        graph, cloud = make_cloud(graph, prev_cloud)

    result =0
    for x in range(N):
        for y in range(N):
            result +=graph[x][y]
    print(result)

if __name__=='__main__':
    main()
