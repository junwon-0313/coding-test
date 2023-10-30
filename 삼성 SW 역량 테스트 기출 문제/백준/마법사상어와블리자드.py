def main():
    # 입력
    global N
    N, M = map(int, input().split())
    # 구슬 그래프
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    # 블리자드
    magic_lst = []
    for _ in range(M):
        magic_lst.append(list(map(int, input().split())))
    # 왼쪽 아래 오른쪽 위
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    # 행렬을 순서에 맞게 리스트로 변환을 위해 방향전환 거리
    dir_lst = []
    for i in range(1, N):
        dir_lst.append(i)
        dir_lst.append(i)
    dir_lst.append(i)

    # 2차원 행렬을 1차원 배열로 변환 -> 구슬 폭발 + 변화하기 쉬워짐
    def graph2lst():
        lst = [0]
        dir_num = 0
        x, y = N // 2, N // 2
        for i in dir_lst:
            for _ in range(i):
                x, y = x + dir[dir_num][0], y + dir[dir_num][1]
                if graph[x][y] == 0:
                    continue
                lst.append(graph[x][y])
            dir_num = (dir_num + 1) % 4
        return lst

    # 1차원 배열을 2차원 행렬로 변환 -> 블리자드를 수행하기 용이함
    def lst2graph():
        # 빈 값에 0을 넣어 만들어줌
        for _ in range(N * N - len(lst)):
            lst.append(0)
        dir_num = 0
        x, y = N // 2, N // 2
        total = 0
        for i in dir_lst:
            for _ in range(i):
                x, y = x + dir[dir_num][0], y + dir[dir_num][1]
                total += 1
                graph[x][y] = lst[total]
            dir_num = (dir_num + 1) % 4
        return graph

    def blizzard(d, s):
        x, y = N // 2, N // 2
        # 상하 좌우
        dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
        for distance in range(1, s + 1):
            nx, ny = x + distance * dx[d], y + distance * dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                graph[nx][ny] = 0
        return graph

    def bomb():
        old = 0
        total_idx = []
        tmp_lst = [0]
        for idx, i in enumerate(lst):
            if i == 0:
                continue
            new = i
            if new == old:
                tmp_lst.append(idx)
            else:
                if len(tmp_lst) >= 4:
                    total_idx.append(tmp_lst)
                    bomb_lst[old] += len(tmp_lst)
                old = new
                tmp_lst = [idx]
        # 한번에 다 터지는 경우
        if len(tmp_lst) >= 4:
            total_idx.append(tmp_lst)
            bomb_lst[old] += len(tmp_lst)
        if len(total_idx) == 0:
            return
        for l in total_idx:
            for idx in l:
                lst[idx] = 0
        return bomb()

    def change():
        total = []
        old = 0
        tmp_lst = [0]
        # print('change',lst)
        for idx, i in enumerate(lst):
            if i == 0:
                continue
            new = i
            if new == old:
                tmp_lst.append(idx)
            else:
                total.append((len(tmp_lst), old))
                old = new
                tmp_lst = [idx]
        total.append((len(tmp_lst), old))
        new_lst = []
        for t in total:
            cnt, num = t
            if num == 0:
                new_lst.append(0)
                continue
            new_lst.append(cnt)
            new_lst.append(num)
        new_lst = new_lst[: N * N]
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

    print(bomb_lst[1] + 2 * bomb_lst[2] + 3 * bomb_lst[3])


if __name__ == "__main__":
    main()
