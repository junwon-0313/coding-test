def main():
    global N, M, K
    N, M, K = map(int, input().split())
    # r*N+c번 리스트에는 질량, 속도, 방향 순으로 파이어볼이 들어있음.
    fire_ball = [[] for _ in range(N**2)]
    # 범위를 0~N-1로 바꿔줌
    for _ in range(M):
        r,c,m,s,d = list(map(int,input().split()))
        fire_ball[(r-1)*N+(c-1)].append((m,s,d))
    dir_lst = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    
    # 최대 2500*2500 
    def move():
        new_fire_ball = [[] for _ in range(N**2)]
        for idx, fire in enumerate(fire_ball):
            # 리스트가 비어있다면 
            if len(fire)==0:
                continue
            for tmp in fire:
                r = idx//N
                c = idx%N
                m,s,d = tmp
                # print(r,c,m,s,d)
                nr, nc = r+s*dir_lst[d][0], c+s*dir_lst[d][1]
                # 범위 1행은 N행과 연결되어 있음!
                if nr<0 or nr>=N:
                    nr = nr%N
                if nc<0 or nc>=N:
                    nc = nc%N
                new_fire_ball[nr*N+nc].append((m,s,d))
        return new_fire_ball  
        
    def after_move():
        new_fire_ball = [[] for _ in range(N**2)]
        for idx, fire in enumerate(fire_ball):
            # 리스트가 비어있다면 
            if len(fire)==0:
                continue
            # 리스트 길이가 1이라면
            elif len(fire)==1:
                new_fire_ball[idx].append(tuple(fire[0]))
            # 같은 칸에 있는 파이어볼은 합쳐짐
            # 나누어진 파이어볼의 질량, 속력, 방향
            elif len(fire) >=2:
                combine_m, combine_s, combine_num = 0,0,len(fire)
                combine_dir = set()
                for tmp in fire:
                    m,s,d = tmp
                    combine_m += m
                    combine_s += s
                    # 홀 짝 저장 최종 길이가 1이면 모두 홀수 or 짝수
                    combine_dir.add(d%2)
                    
                # 질량이 0이면 소멸
                if combine_m//5 ==0:
                    continue
                # 파이어볼은 4개로 나누어짐.
                if len(combine_dir) ==1:
                    for combine_d in [0,2,4,6]:
                        new_fire_ball[idx].append((combine_m//5,combine_s//combine_num,combine_d))  
                else:
                    for combine_d in [1,3,5,7]:
                        new_fire_ball[idx].append((combine_m//5,combine_s//combine_num,combine_d))
        return new_fire_ball
                    
    def measure_m():
        total = 0
        for idx, fire in enumerate(fire_ball):
            # 리스트가 비어있다면 
            if len(fire)==0:
                continue
            for tmp in fire:
                m,_,_ = tmp
                total += m
        return total
        
    for _ in range(K): 
        fire_ball = move()
        fire_ball = after_move()
    print(measure_m())

if __name__=='__main__':
    main()