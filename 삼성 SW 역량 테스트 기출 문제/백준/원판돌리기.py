def main():
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    global N, M
    N, M, T = map(int, input().split())
    graph = [[0] * M]
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    def show_graph(graph):
        print("GRAPH")
        for x in range(1, N + 1):
            for y in range(M):
                print(graph[x][y], end=" ")
            print()

    # print('INIT')
    # show_graph(graph)

    def rotate(xi, di, ki):
        for x in range(1, N + 1):
            # 배수이면 회전
            if x % xi == 0:
                # 시계방향
                if di == 0:
                    for _ in range(ki):
                        graph[x].insert(0, graph[x].pop(-1))
                else:
                    for _ in range(ki):
                        graph[x].append(graph[x].pop(0))

    def find_neighbor():
        new_graph = [[0] * M for _ in range(N + 1)]
        neighbor = False
        for x in range(1, N + 1):
            for y in range(M):
                if graph[x][y] == 0:
                    continue
                for idx in range(4):
                    nx, ny = x + dx[idx], y + dy[idx]
                    # 이웃
                    if ny == M:
                        ny = 0
                    elif ny == -1:
                        ny = M - 1
                    if 1 <= nx <= N:
                        if graph[nx][ny] != 0 and graph[nx][ny] == graph[x][y]:
                            new_graph[x][y] = 0
                            # 한명이라도 있으면
                            neighbor = True
                            break
                else:
                    new_graph[x][y] = graph[x][y]
        return new_graph, neighbor

    def adjust_num():
        t, c = 0, 0
        for x in range(1, N + 1):
            for y in range(M):
                if graph[x][y] == 0:
                    continue
                t += graph[x][y]
                c += 1
        if c == 0:
            return
        m = t / c
        for x in range(1, N + 1):
            for y in range(M):
                if graph[x][y] == 0:
                    continue
                if graph[x][y] > m:
                    graph[x][y] -= 1
                elif graph[x][y] < m:
                    graph[x][y] += 1

    def score():
        total = 0
        for x in range(1, N + 1):
            for y in range(M):
                total += graph[x][y]
        return total

    # T번 회전 수행
    for _ in range(T):
        xi, di, ki = map(int, input().split())
        rotate(xi, di, ki)
        # print('rotate')
        # show_graph(graph)
        graph, is_neighbor = find_neighbor()
        if not is_neighbor:
            adjust_num()
        # print('after')
        # show_graph(graph)
    print(score())


if __name__ == "__main__":
    main()
