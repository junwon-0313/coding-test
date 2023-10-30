def main():
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    # 시작점과 length:2**L을 넘겨주면 해당 범위를 90도 회전한 값을 할당, 길이가 1일 경우는 스킵
    # 0,0부터 줘야함, 모든 격자가 돌아감!!
    def rotate(start, length):
        start_x, start_y = start[0], start[1]
        # 빈 행렬에 값을 저장하고 한번에 업데이트
        rotate_matrix = [[0] * length for _ in range(length)]
        for x in range(length):
            for y in range(length):
                rotate_matrix[y][-1 - x] = graph[x + start_x][y + start_y]
        for x in range(length):
            for y in range(length):
                graph[x + start_x][y + start_y] = rotate_matrix[x][y]

    # 3개 이상 얼음이 있는 칸과 인접해 있지 않으면 얼음의 양이 1 줄어든다.
    def melt():
        # 얼음이 인접해있는 수를 저장하는 배열 생성
        ice = [[0] * len(graph) for _ in range(len(graph))]
        for x in range(len(graph)):
            for y in range(len(graph)):
                if graph[x][y] == 0:
                    continue
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                        if graph[nx][ny] >= 1:
                            ice[x][y] += 1

        for x in range(len(graph)):
            for y in range(len(graph)):
                # 여기에 조건 추가!
                if graph[x][y] == 0:
                    continue
                if ice[x][y] < 3:
                    graph[x][y] -= 1

    # 남아있는 얼음의 양의 합
    def remain_ice():
        remain = 0
        for idx in range(len(graph)):
            remain += sum(graph[idx])
        return remain

    # 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수
    def bfs(start):
        size = 1
        queue = []
        x, y = start[0], start[1]
        queue.append(start)
        visited[x][y] = True
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                    if visited[nx][ny]:
                        continue
                    if graph[nx][ny] >= 1:
                        size += 1
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        return size

    # 입력
    N, Q = map(int, input().split())
    graph = []
    for _ in range(2**N):
        graph.append(list(map(int, input().split())))
    L_lst = list(map(int, input().split()))
    # print('@@@@@@@@@BEFORE@@@@@@@@@@@@@@@')
    # for x in range(2**N):
    #     for y in range(2**N):
    #         print(graph[x][y], end =' ')
    #     print()

    # 파이어스톰 Q번 시전
    for L in L_lst:
        length = 2**L
        # 시계 방향 90도 회전
        # 홀수
        if L == 0:
            melt()
            continue
        for x in range(0, 2**N, length):
            for y in range(0, 2**N, length):
                rotate((x, y), length)
        melt()
    # 1. 남아있는 얼음의 합
    print(remain_ice())
    # 2. 가장 큰 덩어리가 차지하는 칸의 개수, 없을 경우 0!
    ice_size = [0]
    visited = [[False] * len(graph) for _ in range(len(graph))]
    for x in range(len(graph)):
        for y in range(len(graph)):
            if visited[x][y]:
                continue
            if graph[x][y] >= 1:
                ice_size.append(bfs((x, y)))

    print(max(ice_size))

    # print('@@@@@@@@@AFTER@@@@@@@@@@@@@@@')
    # for x in range(2**N):
    #     for y in range(2**N):
    #         print(graph[x][y], end =' ')
    #     print()


if __name__ == "__main__":
    main()
