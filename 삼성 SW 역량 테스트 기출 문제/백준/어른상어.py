def main():
    global N, M, k
    N, M, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    direction = [0]
    direction.extend(list(map(int, input().split())))
    # 상하좌우일때 우선순위
    priority_lst = [[0] for _ in range(M + 1)]
    for idx in range(1, M + 1):
        for _ in range(4):
            priority_lst[idx].append(list(map(int, input().split())))
    shark_out = []
    smell_graph = [[[0, 0]] * N for _ in range(N)]
    # 1 2 3 4 위 아래 왼 오
    dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]

    def shark_smell():
        for x in range(N):
            for y in range(N):
                if graph[x][y] != 0:
                    smell_graph[x][y] = [-k, graph[x][y]]

    def move_shark():
        new_graph = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if graph[x][y] != 0:
                    # 해당 번호와 가리키고 있는 방향에 따른 우선순위 조사 # 아무 흔적도 없을 경우
                    for idx in priority_lst[graph[x][y]][direction[graph[x][y]]]:
                        nx, ny = x + dx[idx], y + dy[idx]
                        if 0 <= nx < N and 0 <= ny < N and smell_graph[nx][ny][0] >= 0:
                            if new_graph[nx][ny] == 0:
                                new_graph[nx][ny] = graph[x][y]
                                direction[graph[x][y]] = idx
                            elif new_graph[nx][ny] > graph[x][y]:
                                shark_out.append(new_graph[nx][ny])
                                new_graph[nx][ny] = graph[x][y]
                                direction[graph[x][y]] = idx
                            else:
                                shark_out.append(graph[x][y])
                            break
                    else:
                        for idx in priority_lst[graph[x][y]][direction[graph[x][y]]]:
                            nx, ny = x + dx[idx], y + dy[idx]
                            if (
                                0 <= nx < N
                                and 0 <= ny < N
                                and smell_graph[nx][ny][1] == graph[x][y]
                            ):
                                if new_graph[nx][ny] == 0:
                                    new_graph[nx][ny] = graph[x][y]
                                    direction[graph[x][y]] = idx
                                elif new_graph[nx][ny] > graph[x][y]:
                                    shark_out.append(new_graph[nx][ny])
                                    new_graph[nx][ny] = graph[x][y]
                                    direction[graph[x][y]] = idx
                                else:
                                    shark_out.append(graph[x][y])
                                break
        return new_graph

    def after_sec():
        for x in range(N):
            for y in range(N):
                smell_graph[x][y][0] += 1

    # 0초 ~ 1000초까지 체크
    for time in range(1001):
        if len(shark_out) == M - 1:
            print(time)
            return
        shark_smell()
        graph = move_shark()
        after_sec()
    else:
        print(-1)


if __name__ == "__main__":
    main()
