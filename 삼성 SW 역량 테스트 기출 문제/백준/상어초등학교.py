def main():
    # 입력
    global N 
    N = int(input())
    student_lst = [] # 학생 순서
    like_lst = [[] for _ in range(N**2+1)]
    graph = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(N*N):
        student, l1,l2,l3,l4 = list(map(int,input().split()))
        student_lst.append(student)
        like_lst[student].extend([l1,l2,l3,l4])
    # print(student_lst)
    # print(like_lst)
    
    # 학생 번호가 주어지면 탐색
    def find_place(num):
        dx, dy = [1,-1,0,0], [0,0,1,-1]
        total_pos = []
        for x in range(1,N+1):
            for y in range(1, N+1):
                # 빈칸이 아닐 경우
                if graph[x][y]!=0:
                    continue
                like = 0
                empty = 0
                # 주변 탐색
                for idx in range(4):
                    nx, ny = x+dx[idx], y+dy[idx]
                    if nx<1 or nx >N or ny<1 or ny>N:
                        continue
                    # 주변에 학생이 좋아하는 사람이 있는지 확인
                    if graph[nx][ny] in like_lst[num]:
                        like+=1
                    # 주변이 비어있는지 확인
                    if graph[nx][ny] ==0:
                        empty+=1
                total_pos.append([like,empty,x,y])
        _,_, pos_x, pos_y = sorted(total_pos, key=lambda x:(-x[0],-x[1],x[2],x[3]))[0]
                # 조건문에 빠진 조건이 많음..
                # # 1번 조건
                # if like >final_like:
                #     final_like = like
                #     final_x, final_y = x,y
                #     continue
                    
                # # 2번 조건
                # if like == final_like and empty> final_empty:
                #     final_empty = empty
                #     final_x, final_y = x, y
                #     continue
                
                # # 3번 조건 1
                # if like == final_like and empty== final_empty and x<final_x:
                #     final_x = x
                #     continue
                # # 2
                # if like == final_like and empty== final_empty and x==final_x and y<final_y:
                #     final_y = y
                #     continue
        
        return pos_x, pos_y
    
    def satisfaction(num,x,y):
        dx, dy = [1,-1,0,0], [0,0,1,-1]
        like = 0
        # 주변에 좋아하는 학생이 몇명인지 확인
        for idx in range(4):
            nx, ny = x+dx[idx], y+dy[idx]
            if nx<1 or nx >N or ny<1 or ny>N:
                continue
            # 주변에 학생이 좋아하는 사람이 있는지 확인
            if graph[nx][ny] in like_lst[num]:
                like+=1
        return like
                
    for num in student_lst:
        pos_x, pos_y = find_place(num)
        graph[pos_x][pos_y] = num


    total_satisfaction = 0
    for x in range(1,N+1):
        for y in range(1, N+1):
            satis = satisfaction(graph[x][y], x,y)
            if satis ==0:
                total_satisfaction+=0
            elif satis ==1:
                total_satisfaction+=1
            elif satis ==2:
                total_satisfaction+=10
            elif satis ==3:
                total_satisfaction+=100
            elif satis ==4:
                total_satisfaction+=1000
    print(total_satisfaction)
    
    # print('@@@@')
    # for x in range(1,N+1):
    #     for y in range(1, N+1):
    #         print(graph[x][y], end = ' ')
    #     print()
    
if __name__=='__main__':
    main()
    