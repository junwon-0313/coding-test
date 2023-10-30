# 모든 출발지는 다르고 출발지와 목적지는 다르다
# 목적지가 출발지가 될 수 있음.
# 출발지 도착지 -> 리스트 + 출발지 방문처리
from collections import deque


def main():
    global N, M, fuel
    N, M, fuel = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    taxi_x, taxi_y = map(int, input().split())
    taxi_x -= 1
    taxi_y -= 1
    passenger = dict()
    for _ in range(M):
        start_x, start_y, final_x, final_y = list(map(int, input().split()))
        passenger[(start_x - 1, start_y - 1)] = (final_x - 1, final_y - 1)

    # 택시 위치, 거리
    # 최단 거리!! queue를 사용
    def bfs(s):
        # 상왼우하
        dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
        queue = deque([s])
        visited = [[False] * N for _ in range(N)]
        visited[s[0]][s[1]] = True
        passenger_lst = []
        while queue:
            x, y, distance = queue.popleft()
            if (x, y) in passenger.keys():
                passenger_lst.append([distance, x, y])
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
        if len(passenger_lst) == 0:
            return 1e9, 0, 0
        else:
            return sorted(passenger_lst)[0]

    def move_destination(s, final_x, final_y):
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        queue = deque([s])
        visited = [[False] * N for _ in range(N)]
        visited[s[0]][s[1]] = True
        while queue:
            x, y, distance = queue.popleft()
            visited[x][y] = True
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
        # 닿을 수 없는 경우
        return 1e9

    for _ in range(M):
        # 가까운 승객을 찾음
        distance, taxi_x, taxi_y = bfs([taxi_x, taxi_y, 0])

        # print('가까운 승객, 거리, 좌표',distance,taxi_x,taxi_y)
        if fuel <= distance:
            result = -1
            break
        fuel -= distance
        final_x, final_y = passenger[(taxi_x, taxi_y)]
        del passenger[(taxi_x, taxi_y)]
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
