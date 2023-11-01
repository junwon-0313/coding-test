def main():
    dx, dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
    org_fish_num = []
    org_fish_dir = []
    for _ in range(4):
        lst = list(map(int, input().split()))
        org_fish_num.append(lst[::2])
        org_fish_dir.append(lst[1::2])
    org_fish_lst = [[] for _ in range(17)]
    for x in range(4):
        for y in range(4):
            org_fish_lst[org_fish_num[x][y]]= [x,y]
    print(org_fish_lst)
    # 상어가 먹은 물고기양 저장
    total_lst =[]
    eat_lst =[]
    # 상어의 위치와 먹은 물고기를 반환
    # 지역 변수로
    def move_fish(shark_pos, eat_lst, fish_lst, fish_num, fish_dir):
        for idx in range(1,17):
            if idx in eat_lst:
                continue
            # 방향이랑 좌표가 같이 바뀌어야함
            x,y = fish_lst[idx]
            direction = fish_dir[x][y]-1
            for angle in range(8):
                direction = (direction+angle)%8
                nx,ny = x+dx[direction], y+ dy[direction]
                # 위치 변경 후, break
                if 0<=nx<4 and 0<=ny<4 and [nx,ny] !=shark_pos:
                    fish_lst[idx]=[nx,ny]
                    fish_lst[fish_num[nx][ny]] =[x,y]
                    fish_num[x][y], fish_num[nx][ny] = fish_num[nx][ny],fish_num[x][y]
                    fish_dir[x][y], fish_dir[nx][ny]= fish_dir[nx][ny], fish_dir[x][y]
                    break
    def back_fish(shark_pos, eat_lst, fish_lst, fish_num, fish_dir):
        for idx in range(16,0,-1):
            if idx in eat_lst:
                continue
            # 방향이랑 좌표가 같이 바뀌어야함
            x,y = fish_lst[idx]
            direction = fish_dir[x][y]-1
            for angle in range(8):
                direction = (direction-angle)%8
                nx,ny = x-dx[direction], y-dy[direction]
                # 위치 변경 후, break
                if 0<=nx<4 and 0<=ny<4 and [nx,ny] !=shark_pos:
                    fish_lst[idx]=[nx,ny]
                    fish_lst[fish_num[nx][ny]] =[x,y]
                    fish_num[x][y], fish_num[nx][ny] = fish_num[nx][ny],fish_num[x][y]
                    fish_dir[x][y], fish_dir[nx][ny]= fish_dir[nx][ny], fish_dir[x][y]
                    break

    def move_shark(shark_pos, eat_lst, fish_lst, fish_num, fish_dir):
        # 물고기 이동
        move_fish(shark_pos,eat_lst, fish_lst, fish_num, fish_dir)
        shark_x, shark_y = shark_pos
        shark_dir= fish_dir[shark_x][shark_y]-1
        for dis in range(1,4):
            shark_nx, shark_ny = shark_x+dis*dx[shark_dir], shark_y+dis*dy[shark_dir]
            if shark_nx<0 or shark_nx>3 or shark_ny<0 or shark_ny>3:
                continue
            if fish_num[shark_nx][shark_ny] in eat_lst:
                continue
            if 1<=fish_num[shark_nx][shark_ny]<=16:
                fish_num[shark_x][shark_y]=0
                eat_lst.append(fish_num[shark_nx][shark_ny])
                print('BEFORE: fish_num')
                for x in range(4):
                    for y in range(4):
                        print(fish_num[x][y],end=' ')
                    print()
                move_shark(shark_pos, eat_lst, fish_lst, fish_num, fish_dir)
                eat_lst.pop()
                back_fish([shark_x,shark_y],eat_lst, fish_lst, fish_num, fish_dir)
                print('AFTER: fish_num')
                for x in range(4):
                    for y in range(4):
                        print(fish_num[x][y],end=' ')
                    print()
        total_lst.append(sum(eat_lst))

        
    def copy_graph(graph):
        new_graph = [[0,0,0,0] for _ in range(4)]
        for x in range(4):
            for y in range(4):
                new_graph[x][y] = graph[x][y]
        return new_graph

        

    # 0,0 위치 물고기를 먹고 해당 방향을 가진다.
    shark_pos =[0,0]
    eat_lst = [org_fish_num[0][0]]
    move_fish(shark_pos, eat_lst, org_fish_lst, org_fish_num, org_fish_dir)
    print('BEFORE: fish_num')
    for x in range(4):
        for y in range(4):
            print(org_fish_num[x][y],end=' ')
        print()
    back_fish(shark_pos, eat_lst, org_fish_lst, org_fish_num, org_fish_dir)
    print('BEFORE: fish_num')
    for x in range(4):
        for y in range(4):
            print(org_fish_num[x][y],end=' ')
        print()
    
    # move_shark(shark_pos, eat_lst, org_fish_lst, org_fish_num, org_fish_dir)
    

    print(total_lst)
if __name__ =='__main__':
    main()