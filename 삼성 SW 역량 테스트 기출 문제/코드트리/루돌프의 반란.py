# 시간 복잡도: 행렬로 구현 후, 탐색하며 문제 해결시 50*50*300 -> 1초 이내 가능
# 리스트로 구현: santa_lst의 0번째는 사용x, 1번째는 첫번째 산타의 좌표, 2번째 원소는 두번째 산타,...
# enumerate를 사용하자!
def main():
    santa_direction = [(-1,0),(0,1), (1,0),(0,-1)]
    # 재귀 함수로 반복 구현
    # 같은 방향으로 계속 가므로 종료 조건 x
    def interaction(santa_num, dx,dy):
        # 상호작용으로 밀려날 떄는 해당 좌표가 이미 값으로 채워짐
        x,y = santa_lst[santa_num]
        nx, ny = x+dx, y+dy
        #범위를 넘어가면
        if nx<1 or nx>N or ny<1 or ny>N:
            out_lst.append(santa_num)
            santa_lst[santa_num] =(-1,-1)
            return
        santa_lst[santa_num] = [nx,ny]
        for idx, santa_pos in enumerate(santa_lst[1:]):
            if santa_num ==idx+1:
                continue
            if idx+1 in out_lst:
                continue
            if [nx,ny]==santa_pos:
                interaction(idx+1,dx,dy)
        

    def crash_rudolph(x,y,dx,dy, santa_num):
        score[santa_num]+=C
        shock_lst[santa_num]=-2
        # 다음 좌표
        nx,ny = x+C*dx, y+C*dy
        if nx<1 or nx>N or ny<1 or ny>N:
            out_lst.append(santa_num)
            santa_lst[santa_num] =(-1,-1)
            return
        santa_lst[santa_num] = [nx,ny]
        for idx, santa_pos in enumerate(santa_lst[1:]):
            if idx+1 == santa_num:
                continue
            if idx+1 in out_lst:
                continue
            if [nx,ny]==santa_pos:
                interaction(idx+1,dx,dy)
        
        
    def move_rudolph():
        nonlocal rudolph_pos
        ru_x, ru_y = rudolph_pos
        near_santa=[]
        # 가장 가까운 산타에게 돌진
        for idx, santa_pos in enumerate(santa_lst[1:]):
            # out_lst에 없으면 범위를 벗어나지 않음!
            if idx+1 in out_lst:
                continue
            near_santa.append((santa_pos[0],santa_pos[1],(ru_x-santa_pos[0])**2+(ru_y-santa_pos[1])**2,idx+1))
        # 조건에 맞게 정렬 후 추출
        sa_x, sa_y, _, santa_num = sorted(near_santa, key = lambda x: (x[2],-x[0],-x[1]))[0]
        if sa_x<ru_x:
            dx=-1
        elif sa_x>ru_x:
            dx=1
        else:
            dx=0
        if sa_y<ru_y:
            dy=-1
        elif sa_y>ru_y:
            dy=1
        else:
            dy=0
        ru_x, ru_y = ru_x+dx, ru_y+dy
        #루돌프 위치 갱신
        rudolph_pos=[ru_x,ru_y]
        # 도착 지점에 산타가 있을 때
        if ru_x == sa_x and ru_y==sa_y:
            crash_rudolph(sa_x,sa_y,dx,dy, santa_num)
            
    def crash_santa(x,y,dx,dy,santa_num):
        score[santa_num]+=D
        shock_lst[santa_num]=-2
        # 다음 좌표
        nx,ny = x-D*dx, y-D*dy
        if nx<1 or nx>N or ny<1 or ny>N:
            out_lst.append(santa_num)
            santa_lst[santa_num] =(-1,-1)
            return
        santa_lst[santa_num] = [nx,ny]
        for idx, santa_pos in enumerate(santa_lst[1:]):
            if santa_num == idx+1:
                continue
            if idx+1 in out_lst:
                continue
            if [nx,ny]==santa_pos:
                interaction(idx+1,-dx,-dy)
        
        
    def move_santa(santa_num):
        nonlocal rudolph_pos
        ru_x, ru_y = rudolph_pos
        x,y = santa_lst[santa_num][0], santa_lst[santa_num][1]
        dis = (ru_x-x)**2+(ru_y-y)**2
        santa_dir = []
        for idx in range(4):
            tf =False
            nx, ny = x+ santa_direction[idx][0],y+santa_direction[idx][1]
            # 범위를 넘어가면
            if nx<1 or nx>N or ny<1 or ny>N:
                continue
            # 다른 산타가 있다면
            for num, santa_pos in enumerate(santa_lst[1:]):
                if num+1 ==santa_num:
                    continue
                if num+1 in out_lst:
                    continue
                if [nx,ny]==santa_pos:
                    tf=True
            if tf:
                continue       
            if dis > (ru_x-nx)**2+(ru_y-ny)**2:
                santa_dir.append(((ru_x-nx)**2+(ru_y-ny)**2,idx))
        if len(santa_dir)==0:
            return
        d = sorted(santa_dir, key = lambda x:(x[0],x[1]))[0][1]
        dx, dy = santa_direction[d][0],santa_direction[d][1]
        nx, ny = x+dx, y+dy
        santa_lst[santa_num]=[nx,ny]

        if nx==ru_x and ny == ru_y:
            crash_santa(nx,ny, dx,dy, santa_num)
    
    # 전역 변수로 설정
    global N, M, P, C, D
    N,M,P,C,D = map(int, input().split())
    ru_x, ru_y = map(int, input().split())
    rudolph_pos=[ru_x,ru_y]
    santa_lst = [[] for _ in range(P+1)]
    score = [0 for _ in range(P+1)]
    out_lst = []
    shock_lst = [0 for _ in range(P+1)]
    for _ in range(P):
        num, x, y = map(int,input().split())
        santa_lst[num] = [x,y] 
        
    for m in range(M):    
        if len(out_lst)==P:
            break
        move_rudolph()
        for i in range(1,P+1):
            if i in out_lst:
                continue
            if shock_lst[i]<0:
                continue
            move_santa(i)
            
        # 살아있으면 점수 +1
        # 1초 지났으면 회복 +1
        for i in range(1,P+1):
            if i in out_lst:
                continue
            shock_lst[i]+=1
            score[i]+=1

    # 점수 출력
    for i in range(1, P+1):
        print(score[i], end=' ')

if __name__=="__main__":
    main()