def main():
    def make_curve(x, y, d, g, point_lst):
        dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        dir_lst = [d]
        nx, ny = x + dir[d][0], y + dir[d][1]
        point_lst.add((x, y))
        point_lst.add((nx, ny))
        x, y = nx, ny
        for i in range(g):
            for direction in dir_lst[::-1]:
                direction = (direction + 1) % 4
                dir_lst.append(direction)
                nx, ny = x + dir[direction][0], y + dir[direction][1]
                point_lst.add((x, y))
                point_lst.add((nx, ny))
                x, y = nx, ny
        return point_lst

    # 입력
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    # 좌표들을 중복되지 않게 저장
    point_lst = set()
    for i in range(N):
        point_lst = make_curve(lst[i][0], lst[i][1], lst[i][2], lst[i][3], point_lst)

    # 정사각형 개수 구하기!
    # 4 꼭짓점이 드래곤 커브의 일부면 됨!
    point_lst = list(point_lst)
    # 정렬
    sorted_lst = sorted(point_lst, key=lambda x: (x[0], x[1]))
    result = 0
    # 정사각형을 만들기 위해서는 4꼭짓점의 좌표가 필요함
    # 왼쪽위부터 시작해서 중복되지 않게 검사!
    for start in sorted_lst:
        x, y = start[0], start[1]
        if (
            ((x + 1, y) in sorted_lst)
            and ((x + 1, y + 1) in sorted_lst)
            and ((x, y + 1) in sorted_lst)
        ):
            result += 1
    print(result)


if __name__ == "__main__":
    main()
