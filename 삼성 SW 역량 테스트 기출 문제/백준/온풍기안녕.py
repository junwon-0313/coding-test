def main():
    # 오, 왼, 위, 아래
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    # 온도, 온풍기 위치, 방향
    # 벽이랑 범위를 초과하지 않으면 온풍기!
    # BFS!! 방문처리, 5까지의 깊이, 재귀 stack을 사용하는 dfs보다 queue를 사용하는 것이 편리
    def fan(start, d, wall):
        # cnt=0이면 종료
        r, c = len(temp_graph), len(temp_graph[0])
        visited = [[False] * c for _ in range(r)]
        # bfs로 해보기
        x, y = start[0], start[1]
        dx, dy = direction[d][0], direction[d][1]
        queue = [(x + dx, y + dy, 5)]

        while queue:
            x, y, cnt = queue.pop(0)
            if cnt <= 0:
                continue
            if x < 0 or x > r - 1 or y < 0 or y > c - 1:
                continue

            if visited[x][y]:
                continue
            visited[x][y] = True
            temp_graph[x][y] += cnt
            # 직진
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if tuple([(x, y), (nx, ny)]) not in wall:
                    queue.append((nx, ny, cnt - 1))

            # 대각선1
            ux1, uy1 = x + dy, y + dx
            ux2, uy2 = nx + dy, ny + dx
            if 0 <= ux2 < r and 0 <= uy2 < c:
                if (
                    tuple([(x, y), (ux1, uy1)]) not in wall
                    and tuple([(ux2, uy2), (ux1, uy1)]) not in wall
                ):
                    queue.append((ux2, uy2, cnt - 1))

            # 대각선1
            dx1, dy1 = x - dy, y - dx
            dx2, dy2 = nx - dy, ny - dx
            if 0 <= dx2 < r and 0 <= dy2 < c:
                if (
                    tuple([(x, y), (dx1, dy1)]) not in wall
                    and tuple([(dx1, dy1), (dx2, dy2)]) not in wall
                ):
                    queue.append((dx2, dy2, cnt - 1))

    # 온도 조절
    def adjust_temp(temp_graph, wall):
        # 오른쪽, 아래 방향만 서치
        dx, dy = (0, 1), (1, 0)
        # 임시 저장 후, 일괄 업데이트, 여기서 인덱스 에러! 잘 체크하기
        tmp_graph = [[0] * len(temp_graph[0]) for _ in range(len(temp_graph))]
        for x in range(len(temp_graph)):
            for y in range(len(temp_graph[0])):
                for k in range(2):
                    # 오른쪽
                    nx, ny = x + dx[k], y + dy[k]
                    if (
                        nx < 0
                        or nx > len(temp_graph) - 1
                        or ny < 0
                        or ny > len(temp_graph[0]) - 1
                    ):
                        continue
                    if tuple([(x, y), (nx, ny)]) in wall:
                        continue
                    if temp_graph[nx][ny] >= temp_graph[x][y]:
                        tmp_graph[nx][ny] -= (
                            temp_graph[nx][ny] - temp_graph[x][y]
                        ) // 4
                        tmp_graph[x][y] += (temp_graph[nx][ny] - temp_graph[x][y]) // 4
                    else:
                        tmp_graph[x][y] -= (temp_graph[x][y] - temp_graph[nx][ny]) // 4
                        tmp_graph[nx][ny] += (
                            temp_graph[x][y] - temp_graph[nx][ny]
                        ) // 4

        for x in range(len(temp_graph)):
            for y in range(len(temp_graph[0])):
                temp_graph[x][y] += tmp_graph[x][y]

        # 모서리 +1
        for x in (0, -1):
            for y in (0, -1):
                if temp_graph[x][y] >= 1:
                    temp_graph[x][y] += 1
        # 각변 -1
        for x in (0, -1):
            for y in range(len(temp_graph[0])):
                if temp_graph[x][y] >= 1:
                    temp_graph[x][y] -= 1

        for x in range(len(temp_graph)):
            for y in (0, -1):
                if temp_graph[x][y] >= 1:
                    temp_graph[x][y] -= 1

        return temp_graph

    # 모든 범위가 넘는지 확인
    def check(temp_graph, search_lst, K):
        for i in search_lst:
            x, y = i[0], i[1]
            if temp_graph[x][y] < K:
                return False
        return True

    R, C, K = map(int, input().split())
    graph = []
    for i in range(R):
        graph.append(list(map(int, input().split())))
    W = int(input())
    # 벽
    wall = set()
    for i in range(W):
        x, y, w = map(int, input().split())
        if w == 0:
            wall.add(tuple([(x - 1, y - 1), (x - 2, y - 1)]))
            wall.add(tuple([(x - 2, y - 1), (x - 1, y - 1)]))
        elif w == 1:
            wall.add(tuple([(x - 1, y - 1), (x - 1, y)]))
            wall.add(tuple([(x - 1, y), (x - 1, y - 1)]))

    # 온도를 조사해야 하는 칸
    search_lst = []
    # 온풍기 위치와 방향
    fan_lst = []
    # 온도
    temp_graph = [[0] * C for _ in range(R)]

    # 0~R-1
    for x in range(R):
        for y in range(C):
            if graph[x][y] == 0:
                continue
            elif 1 <= graph[x][y] <= 4:
                fan_lst.append((x, y, graph[x][y]))
            else:
                search_lst.append((x, y))

    chocolate = 0
    while True:
        # 온풍기 작동
        for idx in range(len(fan_lst)):
            x, y, dir = fan_lst[idx]
            fan((x, y), dir - 1, wall)
        # 온도 조절
        temp_graph = adjust_temp(temp_graph, wall)
        # 초콜릿 먹기
        chocolate += 1
        # 체크 종료 조건
        if check(temp_graph, search_lst, K):
            break
        if chocolate > 100:
            chocolate = 101
            break
    # print(temp_graph)
    print(chocolate)


if __name__ == "__main__":
    main()
