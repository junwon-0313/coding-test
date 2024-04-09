n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dxs, dys = [-1,1,0,0],[0,0,-1,1]
block = [[0,1,2,3],
         [3,2,1,0],
         [2,3,0,1]]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move(position, d, time):
    x, y = position
    while True:
        time+=1 # 시간 증가
        nx, ny = x+dxs[d], y+dys[d]
        if not in_range(nx,ny):
            break
        d = block[graph[nx][ny]][d]
        x, y = nx, ny # 좌표 업데이트
    return time

# -1, 0~n-1
ans = -1
for pos in range(n):
    # print('time', move((-1,pos),1,0))
    ans = max(ans, move((-1,pos),1,0)) # 위쪽
    ans = max(ans, move((n,pos),0,0)) # 아래쪽
    ans = max(ans, move((pos,-1),3,0)) # 왼쪽
    ans = max(ans, move((pos,n),2,0)) # 오른쪽
print(ans)
