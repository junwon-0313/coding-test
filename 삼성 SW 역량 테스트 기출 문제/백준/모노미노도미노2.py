def main():
    N = int(input())
    block_lst = []
    for _ in range(N):
        tmp = []
        t, x, y = map(int, input().split())
        tmp.append([t, x, y])
        if t == 2:
            tmp.append([t, x, y + 1])
        elif t == 3:
            tmp.append([t, x + 1, y])
        block_lst.append(tmp)
    # 전역 변수!!
    red = [[0] * 4 for _ in range(4)]
    blue = [[0] * 6 for _ in range(4)]
    green = [[0] * 4 for _ in range(6)]
    score = 0

    # 출력 확인용
    def print_domino():
        for x in range(10):
            for y in range(10):
                if x <= 3 and y <= 3:
                    print(red[x][y], end=" ")
                elif x <= 3 and 3 < y:
                    print(blue[x][y - 4], end=" ")
                elif 3 < x and y <= 3:
                    print(green[x - 4][y], end=" ")
            print()

    # 블록 개수 세기
    def count_block(graph):
        cnt = 0
        for x in range(len(graph)):
            for y in range(len(graph[0])):
                if graph[x][y] == 1:
                    cnt += 1
        return cnt

    # 블록을 쌓음
    def stack_block(block):
        # blue는 x가 고정
        # green은 y가 고정
        # 블록의 길이가 2 이상이 경우에는 둘 다 체크!
        # 벽이나 다른 블록
        max_blue = []
        max_green = []
        # 마지막 쌓을 위치 결정
        for _, x, y in block:
            for idx in range(6):
                if blue[x][idx] == 1:
                    max_blue.append(idx - 1)
                    break
            else:
                max_blue.append(5)
            for idx in range(6):
                if green[idx][y] == 1:
                    max_green.append(idx - 1)
                    break
            else:
                max_green.append(5)
        # 블록을 각각 쌓아줌
        for t, x, y in block:
            blue[x][min(max_blue)] = 1
            green[min(max_green)][y] = 1
            if t == 2:
                blue[x][min(max_blue) - 1] = 1
            elif t == 3:
                green[min(max_green) - 1][y] = 1

    # 테트리스, 한 줄에 값이 생기면 점수 획득 -> 해당 위칸을 한칸씩 밀기
    def pop_block(score):
        # blue는 한 열이 1일 경우
        blue_cols = []
        for y in range(6):
            for x in range(4):
                if blue[x][y] == 0:
                    break
            else:
                blue_cols.append(y)

        # green은 한 행이 1일 경우,
        green_rows = []
        for x in range(6):
            for y in range(4):
                if green[x][y] == 0:
                    break
            else:
                green_rows.append(x)
                
        score = score + len(blue_cols) + len(green_rows)
        return blue_cols, green_rows, score
    
    # 0~1번 행과 열에 값이 있을 경우 1~2칸 밀기
    def push_block(blue_cols, green_rows):
        new_blue = [[0] * 6 for _ in range(4)]
        new_green = [[0] * 4 for _ in range(6)]
        blue_over, green_over = 0, 0
        for y in range(2):
            for x in range(4):
                if blue[x][y] == 1:
                    blue_over += 1
                    break

        for x in range(2):
            for y in range(4):
                if green[x][y] == 1:
                    green_over += 1

        for x in range(4):
            for y in range(6 - blue_over):
                new_blue[x][y + blue_over] = blue[x][y]

        for x in range(6 - green_over):
            for y in range(4):
                new_green[x + green_over][y] = green[x][y]
        # 만약 사라지는 칸에 6번이나 5번이 포함되는 경우, 
        new_blue_cols = []
        new_green_rows = []
        if blue_over==1:
            for i in blue_cols:
                if i ==5:
                    continue
                new_blue_cols.append(i+1)
        elif blue_over ==2:
            for i in blue_cols:
                if i==4 or i ==5 :
                    continue
                new_blue_cols.append(i+2)
        if green_over==1:
            for i in green_rows:
                if i ==5:
                    continue
                new_green_rows.append(i+1)
        elif green_over ==2:
            for i in green_rows:
                if i==4 or i ==5:
                    continue
                new_green_rows.append(i+2)
        if blue_over ==0:
            new_blue_cols = blue_cols
        if green_over ==0:
            new_green_rows = green_rows
        return new_blue, new_green, new_blue_cols, new_green_rows

    def move_down(blue, green, blue_cols, green_rows):
        if len(blue_cols) == 0:
            pass
        else:
            new_blue = [[0] * 6 for _ in range(4)]
            bs = len(blue_cols)
            col = max(blue_cols)
            for x in range(4):
                for y in range(6):
                    if y <= col - bs:
                        new_blue[x][y + bs] = blue[x][y]
                    elif y > col:
                        new_blue[x][y] = blue[x][y]
            blue = new_blue
        if len(green_rows) == 0:
            pass
        else:
            new_green = [[0] * 4 for _ in range(6)]
            gs = len(green_rows)
            row = max(green_rows)
            for x in range(6):
                for y in range(4):
                    if x <= row - gs:
                        new_green[x + gs][y] = green[x][y]
                    elif x > row:
                        new_green[x][y] = green[x][y]
            green = new_green
        return blue,green
        
    # print_domino()
    for block in block_lst:
        print('Add block',block)
        stack_block(block)
        blue_cols, green_rows, score = pop_block(score)
        blue, green,blue_cols, green_rows = push_block(blue_cols, green_rows)
        blue, green = move_down(blue, green, blue_cols, green_rows)
        print_domino()
        
    # 결과 출력
    print(score)
    print(count_block(blue) + count_block(green))

if __name__ == "__main__":
    main()
