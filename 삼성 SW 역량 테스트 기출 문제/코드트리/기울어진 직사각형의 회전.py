n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
r, c, m1, m2, m3, m4, d = map(int,input().split())

def print_g():
    for x in range(n):
        for y in range(n):
            print(graph[x][y], end = ' ')
        print()

dxs, dys = [-1,-1,1,1], [1,-1,-1,1]

def rotate_g(r,c,m1,m2,m3,m4,d):
    point1 = (r+dxs[0]*m1, c+dys[0]*m1)
    point2 = (point1[0]+dxs[1]*m2, point1[1]+dys[1]*m2)
    point3 = (point2[0]+dxs[2]*m3, point2[1]+dys[2]*m3)
    if d ==0: # 반시계
        p1 = graph[point1[0]][point1[1]]
        for idx in range(m1,0,-1): #r,c기준으로
            graph[r+dxs[0]*idx][c+dys[0]*idx] = graph[r+dxs[0]*(idx-1)][c+dys[0]*(idx-1)]
        p2 = graph[point2[0]][point2[1]]
        for idx in range(m2,1,-1):
            graph[point1[0]+dxs[1]*idx][point1[1]+dys[1]*idx] = graph[point1[0]+dxs[1]*(idx-1)][point1[1]+dys[1]*(idx-1)]
        graph[point1[0]+dxs[1]][point1[1]+dys[1]] = p1
        p3 = graph[point3[0]][point3[1]]
        for idx in range(m3,1,-1):
            graph[point2[0]+dxs[2]*idx][point2[1]+dys[2]*idx] = graph[point2[0]+dxs[2]*(idx-1)][point2[1]+dys[2]*(idx-1)]
        graph[point2[0]+dxs[2]][point2[1]+dys[2]] = p2
        for idx in range(m4,1,-1):
            graph[point3[0]+dxs[3]*idx][point3[1]+dys[3]*idx] = graph[point3[0]+dxs[3]*(idx-1)][point3[1]+dys[3]*(idx-1)]
        graph[point3[0]+dxs[3]][point3[1]+dys[3]] = p3
    else: # 시계 방향
        p1 = graph[r][c]
        for idx in range(m1): #r,c기준으로
            graph[r+dxs[0]*idx][c+dys[0]*idx] = graph[r+dxs[0]*(idx+1)][c+dys[0]*(idx+1)]
        p2 = graph[point3[0]][point3[1]]
        # point 3
        for idx in range(m4-1):
            graph[point3[0]+dxs[3]*idx][point3[1]+dys[3]*idx] = graph[point3[0]+dxs[3]*(idx+1)][point3[1]+dys[3]*(idx+1)]
        graph[r-dxs[3]][c-dys[3]] = p1
        p3 = graph[point2[0]][point2[1]]
        # point2
        for idx in range(m3-1):
            graph[point2[0]+dxs[2]*idx][point2[1]+dys[2]*idx] = graph[point2[0]+dxs[2]*(idx+1)][point2[1]+dys[2]*(idx+1)]
        graph[point3[0]-dxs[2]][point3[1]-dys[2]] = p2
        for idx in range(m2-1):
            graph[point1[0]+dxs[1]*idx][point1[1]+dys[1]*idx] = graph[point1[0]+dxs[1]*(idx+1)][point1[1]+dys[1]*(idx+1)]
        graph[point2[0]-dxs[1]][point2[1]-dys[1]] = p3

rotate_g(r-1,c-1,m1,m2,m3,m4,d)
print_g()
