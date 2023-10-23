# 방향이 정해져 있음
# 칸 번호에 맞게 행렬을 리스트로 바꾼다.
# 블리자드: 상어가 상하좌우 방향으로 해당 거리만큼 구슬을 제거
# 칸의 번호는 지정되어 있음
# 칸의 번호가 하나작은 곳이 비어있다면 이동 -> 리스트는 자동으로 됨
# 4개 이상 연속하면 구슬을 터트리고 -> 밀고 -> 터트릴 게 없을 때까지 반복!
# 구슬 변화
# 하나의 그룹 -> 구슬의 개수, 그룹의 숫자
# 구슬이 칸을 넘으면 사라짐.
def main():
    global N
    N, M = map(int, input().split())
    # 행렬로 입력받음
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    # 블리자드
    magic_lst = []
    for _ in range(M):
        magic_lst.append(list(map(int, input().split())))
    dir = [(0,-1),(1,0),(0,1),(-1,0)]
    # 행렬을 순서에 맞게 리스트로 변환을 위해 방향전환 거리
    dir_lst = []
    for i in range(1,N):
        dir_lst.append(i)
        dir_lst.append(i)
    dir_lst.append(i)
    
    # 리스트에서 구슬 폭발 및 변화
    def graph2lst():
        lst = [0]
        dir_num = 0
        x,y = N//2, N//2
        for i in dir_lst:
            for _ in range(i):
                x, y = x + dir[dir_num][0], y + dir[dir_num][1]
                if graph[x][y]==0:
                    continue
                lst.append(graph[x][y])
            dir_num = (dir_num+1)%4
        return lst
    
    # 그래프에서 블리자드
    def lst2graph():
        # 빈 값에 0을 넣어 만들어줌
        for _ in range(N*N-len(lst)):
            lst.append(0)
        dir_num = 0
        x,y = N//2, N//2
        total = 0
        for i in dir_lst:
            for _ in range(i):
                x, y = x + dir[dir_num][0], y + dir[dir_num][1]
                total+=1
                graph[x][y] = lst[total]
            dir_num = (dir_num+1)%4
        return graph
        
    def blizzard(d,s):
        x,y = N//2, N//2
        # 상하 좌우 
        dx, dy = [0,-1,1,0,0], [0,0,0,-1,1]
        for distance in range(1,s+1):
            nx,ny = x+distance*dx[d], y+distance*dy[d]
            if 0<=nx<N and 0<= ny <N:
                graph[nx][ny]=0
        # print('@BBBBBBB@@@@')
        # for x in range(N):
        #     for y in range(N):
        #         print(graph[x][y], end = ' ')
        #     print()
        return graph
        
    
    def bomb():
        # print('BOmB', lst)
        old = -1
        total_idx = []
        tmp_lst = []
        for idx, i in enumerate(lst):
            new = i
            if new ==old:
                tmp_lst.append(idx)
            else:
                if len(tmp_lst)>=4:
                    total_idx.append(tmp_lst)
                    bomb_lst[old]+=len(tmp_lst)
                old = new
                tmp_lst=[idx]
        # 한번에 다 터지는 경우
        if len(tmp_lst)>=4:
                total_idx.append(tmp_lst)
                bomb_lst[old]+=len(tmp_lst)
        if len(total_idx) ==0:
            return
        for l in total_idx[::-1]:
            for idx in l[::-1]:
                lst.pop(idx)
        return bomb()
    
    def change():
        total = []
        # print('change',lst)
        for idx, i in enumerate(lst):
            if idx ==0:
                old = i
                tmp_lst=[0]
                continue
            new = i
            if new ==old:
                tmp_lst.append(idx)
            else:
                total.append((len(tmp_lst),old))
                old = new
                tmp_lst=[idx]
        total.append((len(tmp_lst),old))
        # print('total',total)
        new_lst = []
        for t in total:
            cnt, num = t
            if num ==0:
                new_lst.append(0)
                continue
            new_lst.append(cnt)
            new_lst.append(num)
        new_lst = new_lst[:N*N]
        # print(new_lst)
        return new_lst

    # 터진 폭탄수, 0만 들어올 경우 예외처리
    bomb_lst = [0 for _ in range(4)]
    
    # 블리자드 -> 동작
    for magic in magic_lst:
        d, s = magic
        graph = blizzard(d, s)
        lst = graph2lst()
        bomb()
        lst = change()
        graph = lst2graph()
        # graph 출력문
        # print('@@@GRAPH@@@@')
        # for x in range(N):
        #     for y in range(N):
        #         print(graph[x][y], end = ' ')
        #     print()
    
    print(bomb_lst[1]+2*bomb_lst[2]+3*bomb_lst[3])

if __name__ == "__main__":
    main()