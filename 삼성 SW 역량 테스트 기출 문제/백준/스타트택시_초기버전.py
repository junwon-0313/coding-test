# 시간초과 문제는 bfs시에 방문처리를 제대로 하지 않았기 때문에 발생함.
# 닿을 수 없는 경우 예외처리! -> 400이 아닌 연료값까지 생각해서 최댓값을 지정해주어야함.
# 두 개의 리스트를 사용하여 출발과 도착을 관리
# 0~N-1 좌표를 사용
# distance_map을 사용 -> bfs사용 등 여러 방법이 존재함.
def main():
    global N, M, fuel
    N, M, fuel = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    taxi_x, taxi_y = map(int, input().split())
    taxi_x -= 1
    taxi_y -= 1
    start = []
    final = []
    for _ in range(M):
        start_x, start_y, final_x, final_y = list(map(int, input().split()))
        start.append([start_x - 1, start_y - 1])
        final.append([final_x - 1, final_y - 1])

    # 택시 위치
    # 최단 거리!! queue를 사용
    def find_passenger(taxi_x, taxi_y):
        passenger_lst = []
        distance_map = bfs([taxi_x, taxi_y, 0])
        for idx, pos in enumerate(start):
            # 번호, 거리, x, y
            passenger_lst.append([idx, distance_map[pos[0]][pos[1]], pos[0], pos[1]])
        num, dis, x, y = sorted(passenger_lst, key=lambda x: (x[1], x[2], x[3]))[0]
        # 태운 승객을 제외하기
        if dis != 1e9:
            start.pop(num)
        return num, dis, x, y

    def bfs(s):
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        queue = [s]
        visited = [[False] * N for _ in range(N)]
        visited[s[0]][s[1]] = True
        distance_map = [[1e9] * N for _ in range(N)]
        while queue:
            x, y, distance = queue.pop(0)
            distance_map[x][y] = distance
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                    continue
                if graph[nx][ny] == 1:
                    continue
                if visited[nx][ny]:
                    continue
                queue.append([nx, ny, distance + 1])
                visited[nx][ny] = True
        return distance_map

    def move_destination(s, final_x, final_y):
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        queue = [s]
        visited = [[False] * N for _ in range(N)]
        visited[s[0]][s[1]] = True
        while queue:
            x, y, distance = queue.pop(0)
            if x == final_x and y == final_y:
                return distance
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                    continue
                if graph[nx][ny] == 1:
                    continue
                if visited[nx][ny]:
                    continue
                queue.append([nx, ny, distance + 1])
                visited[nx][ny] = True
        return 1e9

    for _ in range(M):
        # 가까운 승객을 찾음
        num, distance, taxi_x, taxi_y = find_passenger(taxi_x, taxi_y)
        # print('가까운 승객과의 거리, 좌표',distance,taxi_x,taxi_y)
        if fuel <= distance:
            result = -1
            break
        fuel -= distance
        final_x, final_y = final.pop(num)
        distance = move_destination([taxi_x, taxi_y, 0], final_x, final_y)
        # print('도착지까지 거리', distance, final_x, final_y)
        if fuel < distance:
            result = -1
            break
        fuel += distance
        taxi_x, taxi_y = final_x, final_y
        result = fuel

    print(result)


if __name__ == "__main__":
    main()
