import copy


def main():
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
    fish_num = []
    fish_dir = []
    for _ in range(4):
        lst = list(map(int, input().split()))
        fish_num.append(lst[::2])
        fish_dir.append(lst[1::2])
    fish_lst = [[] for _ in range(17)]
    for x in range(4):
        for y in range(4):
            fish_lst[fish_num[x][y]] = [x, y, fish_dir[x][y] - 1]

    def move_fish(sx, sy, fish_lst):
        for fish in range(1, 17):
            if fish in eat_lst:
                continue
            x, y, dir = fish_lst[fish]
            for idx in range(8):
                new_dir = (dir + idx) % 8
                nx, ny = x + dx[new_dir], y + dy[new_dir]
                if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                    continue
                if [nx, ny] == [sx, sy]:
                    continue
                for num in range(1, 17):
                    if fish_lst[num][:2] == [nx, ny]:
                        change = num
                change_dir = fish_lst[change][2]
                fish_lst[change] = [x, y, change_dir]
                fish_lst[fish] = [nx, ny, new_dir]
                break

    # dfs 재귀, 지역변수 선언
    def move_shark(shark_pos, eat_lst, fish_lst):
        sx, sy, shark_dir = shark_pos
        # 물고기 움직임
        move_fish(sx, sy, fish_lst)
        # 상어 이동
        for dis in range(1, 4):
            nx, ny = sx + dis * dx[shark_dir], sy + dis * dy[shark_dir]
            if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                continue
            for num in range(1, 17):
                if fish_lst[num][:2] == [nx, ny]:
                    fnum = num
            if fnum in eat_lst:
                continue
            if 1 <= fnum <= 16:
                eat_lst.append(fnum)
                shark_pos = fish_lst[fnum][:]
                move_shark(shark_pos, eat_lst, copy.deepcopy(fish_lst))
                eat_lst.pop()
        total_lst.append(sum(eat_lst))

    total_lst = []
    for num in range(1, 17):
        if fish_lst[num][:2] == [0, 0]:
            fnum = num
    eat_lst = [fnum]
    shark_pos = fish_lst[fnum][:]
    move_shark(shark_pos, eat_lst, copy.deepcopy(fish_lst))
    print(max(total_lst))


if __name__ == "__main__":
    main()
