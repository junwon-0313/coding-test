def main():
    # 상어위치는 전역변수로 사용
    global sx, sy

    def move_fish(graph, fish_lst, visited):
        after_move = []
        # 물고기가 존재한다면
        for i in range(len(fish_lst)):
            x, y, dir = fish_lst[i][0], fish_lst[i][1], fish_lst[i][2]
            for j in range(8):
                nx, ny = x + direction[dir - 1 - j][0], y + direction[dir - 1 - j][1]
                # 상어에 막힘
                if nx == sx and ny == sy:
                    continue
                # 범위를 나감
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    continue
                # 물고기 자취 -2-> 최근, -1은 하나 전 ,0이면 지워짐
                if visited[nx][ny] < 0:
                    continue
                if dir - 1 - j < 0:
                    d = dir - j + 8
                else:
                    d = dir - j
                after_move.append((nx, ny, d))
                graph[nx][ny] += 1
                graph[x][y] -= 1
                break
            else:
                after_move.append((x, y, dir))
        return graph, after_move

    def move_shark(graph, sx, sy, visited, after_move):
        # 이동한 세칸 찾고 최종 업데이트
        # 1:상, 2:좌, 3:하, 4:우
        # 같은 곳을 또 방문했을 때, 안오게
        tmp_sx, tmp_sy = sx, sy
        shark_lst = []
        shark_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(4):
            nx1, ny1 = tmp_sx + shark_dir[i][0], tmp_sy + shark_dir[i][1]
            if nx1 < 1 or nx1 > 4 or ny1 < 1 or ny1 > 4:
                continue

            for j in range(4):
                nx2, ny2 = nx1 + shark_dir[j][0], ny1 + shark_dir[j][1]
                if nx2 < 1 or nx2 > 4 or ny2 < 1 or ny2 > 4:
                    continue

                for k in range(4):
                    nx3, ny3 = nx2 + shark_dir[k][0], ny2 + shark_dir[k][1]
                    if nx3 < 1 or nx3 > 4 or ny3 < 1 or ny3 > 4:
                        continue
                    if nx1 == nx3 and ny1 == ny3:
                        shark_fish = graph[nx1][ny1] + graph[nx2][ny2]
                    else:
                        shark_fish = graph[nx1][ny1] + graph[nx2][ny2] + graph[nx3][ny3]

                    shark_m = str(i + 1) + str(j + 1) + str(k + 1)
                    shark_lst.append(((shark_m), shark_fish))

        shark = sorted(shark_lst, key=lambda x: (-x[1], int(x[0])))[0]

        # 상어 이동 + lst에서 특정 문자 제거?
        remove_lst = []
        remove_pos = []
        for i in list(map(int, str(shark[0]))):
            sx += shark_dir[i - 1][0]
            sy += shark_dir[i - 1][1]
            if graph[sx][sy] > 0:
                remove_pos.append((sx, sy))
                graph[sx][sy] = 0
                visited[sx][sy] = -3

        for i in after_move:
            if (i[0], i[1]) in remove_pos:
                continue
            remove_lst.append(i)

        return graph, remove_lst, visited, sx, sy

    # 1~8까지의 자연수
    direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    M, S = map(int, input().split())
    fish_lst = []
    graph = [[0] * 5 for _ in range(5)]
    visited = [[0] * 5 for _ in range(5)]
    for i in range(M):
        fx, fy, d = map(int, input().split())
        graph[fx][fy] += 1
        fish_lst.append((fx, fy, d))

    sx, sy = map(int, input().split())
    # 상어 위치, 이동 경로만 추적 -> 물고기 냄새 -> 제일 많은 물고기를 제외하는 방향(1,1,2), 4
    for i in range(S):
        new_graph, after_move = move_fish(graph, fish_lst, visited)
        graph, remove_lst, visited, sx, sy = move_shark(
            new_graph, sx, sy, visited, after_move
        )

        # 흔적은 2턴이 지나면 사라진다.
        for x in range(1, 5):
            for y in range(1, 5):
                visited[x][y] += 1

        # 복사 마법 진행
        for x in fish_lst:
            graph[x[0]][x[1]] += 1
        fish_lst += remove_lst

    total_fish = 0
    for x in range(1, 5):
        for y in range(1, 5):
            total_fish += graph[x][y]
    print(total_fish)


if __name__ == "__main__":
    main()
