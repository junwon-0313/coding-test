# 체스판과 말 상태는 어떻게 관리할 것인가?
# 말을 순서대로 관리해야함. 위에서부터 왼쪽 
def main():
    N, K = map(int,input().split())
    # 체스판
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    horse = [[[] for _ in range(N)] for _ in range(N)]
    for idx in range(K):
        row, col, dir = map(int,input().split())
        row-=1
        col-=1
        horse[row][col].append((idx+1,dir))
    
    # 출력
    def print_horse_pos():
        print('@@@@@@@@@@@@@@')
        for x in range(N):
            for y in range(N):
                print(horse[x][y], end =' ')
            print()
    print_horse_pos()
    
if __name__ == "__main__":
    main()
