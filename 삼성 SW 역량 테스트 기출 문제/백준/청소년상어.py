import copy
def main():
    dx, dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
    fish_num = []
    fish_dir = []
    for _ in range(4):
        lst = list(map(int, input().split()))
        fish_num.append(lst[::2])
        fish_dir.append(lst[1::2])
    fish_lst = [[] for _ in range(17)]
    for x in range(4):
        for y in range(4):
            fish_lst[fish_num[x][y]]=[x,y,fish_dir[x][y]]
        
    def move_fish(sx,sy): 
        print('move')     
        print(fish_lst)
        for fish in range(1,17):
            if fish in eat_lst:
                continue
            x,y,dir = fish_lst[fish]
            dir -=1
            for idx in range(8):
                dir = (dir+idx)%8
                nx, ny = x+dx[dir], y+dy[dir]
                if nx<0 or nx>3 or ny<0 or ny>3:
                    continue
                if [nx,ny]==[sx,sy]:
                    continue
                change = find([nx,ny])
                fish_lst[fish] = fish_lst[change]
                fish_lst[change] = [x,y,dir+1]
                break
                
    def find(pos):
        for fish in range(1,17):
            if fish_lst[fish][:2]==pos:
                return fish
        return 0
    
    # dfs 재귀, 지역변수 선언
    def move_shark(shark_pos,eat_lst,fish_lst):
        print()
        print(eat_lst)
        print(fish_lst)
        sx,sy,shark_dir = shark_pos
        shark_dir-=1
        # 물고기 움직임
        move_fish(sx,sy)
        # 상어 이동
        for dis in range(1,4):
            nx, ny = sx+dis*dx[shark_dir], sy+dis*dy[shark_dir]
            if nx<0 or nx>3 or ny<0 or ny>3:
                    continue
            if find([nx,ny]) in eat_lst:
                continue
            if 1<= find([nx,ny])<=16:
                eat_lst.append(find([nx,ny]))
                move_shark([nx,ny,fish_lst[find([nx,ny])][2]],eat_lst,copy.deepcopy(fish_lst))
                eat_lst.pop()
        total_lst.append(sum(eat_lst))
    
    total_lst = []
    eat_lst = [find([0,0])]
    move_shark([0,0,fish_lst[find([0,0])][2]],eat_lst,fish_lst)
    print('@@',total_lst)
            
if __name__ =='__main__':
    main()
    
# move_fish에서 fish_lst가 제대로 전달이 안됨.