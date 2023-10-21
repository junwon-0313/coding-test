# 방향이 정해져 있음
# 칸 번호에 맞게 행렬을 리스트로 바꾼다.
# 블리자드: 상어가 상하좌우 방향으로 해당 거리만큼 구슬을 제거
# 칸의 번호는 지정되어 있음
# 칸의 번호가 하나작은 곳이 비어있다면 이동 -> 리스트는 자동으로 됨
# 4개 이상 연속하면 구슬을 터트리고 -> 밀고 -> 터트릴 게 없을 때까지 반복!
# 구슬 변화
# 하나의 그룹 -> 구슬의 개수, 그룹의 숫자
# 구슬이 칸을 넘으면 사라짐.
def main():
    global N
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    blizzard = []
    for _ in range(M):
        blizzard.append(list(map(int, input().split())))
    dir = [(0,-1),(1,0),(0,1),(-1,0)]
    dir_lst = []
    for i in range(1,N):
        dir_lst.append(i)
        dir_lst.append(i)
    dir_lst.append(i)
    lst = [0]
    dir_num = 0
    x,y = N//2, N//2
    for i in dir_lst:
        for _ in range(i):
            x, y = x + dir[dir_num][0], y + dir[dir_num][1]
            lst.append(graph[x][y])
        dir_num = (dir_num+1)%4
    print(lst)
    print(len(lst))

    # 초기 구슬 1,2,3의 개수
    


if __name__ == "__main__":
    main()