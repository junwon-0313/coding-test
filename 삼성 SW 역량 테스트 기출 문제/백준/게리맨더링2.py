def main():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    total_num = 0
    for i in range(N):
        for j in range(N):
            total_num += graph[i][j]
    # 전체 경우에서 차이의 최솟값 저장
    total_min = 1e9
    # 시작점
    for x in range(N):
        for y in range(N):
            # d1, d2 경계a
            for d1 in range(1,N):
                for d2 in range(1,N):
                    # 범위를 벗어날 경우 종료
                    # 꼭짓점이 범위를 나가는 지 체크
                    if y-d1<0 or x+d1+d2>=N or y+d2>=N:
                        continue
                    # 5번 구역 체크
                    visited = [[False]*N for _ in range(N)]
                    nx, ny = x,y
                    for j in range(d2+1):
                        for i in range(d1+1):
                            visited[ny-i][nx+i]=True
                        nx, ny = nx+1, ny+1 
                    nx, ny = x+1,y
                    for j in range(d2):
                        for i in range(d1):
                            visited[ny-i][nx+i]=True
                        nx, ny = nx+1, ny+1
                    # print('@@@')
                    # print(x,y,d1,d2)
                    # for i in range(N):
                    #     for j in range(N):
                    #         print(visited[i][j], end = ' ')
                    #     print()
                    # x,y,d1,d2가 정해짐 -> 전체 돌면서 조건 탐색
                    # 5번 구역
                    area = [0]*5
                    for r in range(N):
                        for c in range(N):
                            
                            if visited[r][c]:
                                continue
                            if 0<=r<x+d1-1 and 0<=c<y:
                                area[0]+=graph[r][c]
                            elif 0<= r<x+d2 and y<=c<N:
                                area[1]+=graph[r][c]
                            elif x+d1-1<=r<N and 0<=c<y-d1+d2-1:
                                area[2]+=graph[r][c]
                            elif x+d2<= r<N and y-d1+d2-1<=c<N:
                                area[3]+=graph[r][c]
                    area[4] = total_num - sum(area)
                    # 최솟값만 유지
                    print(area, sum(area))
                    local_min = max(area) - min(area)
                    print(local_min)
                    if local_min < total_min:
                        total_min = local_min  
                        
    print(total_min)  

if __name__=='__main__':
    main()