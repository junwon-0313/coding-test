import copy

max_score = 0


def main():
    dice = list(map(int, input().split()))
    # 윷놀이 판, 말은 4개
    board = [[i * 2 for i in range(21)]]
    # 10일 때
    board.append([10, 13, 16, 19, 25, 30, 35, 40])
    # 20일 때
    board.append([20, 22, 24, 25, 30, 35, 40])
    # 30일 때
    board.append([30, 28, 27, 26, 25, 30, 35, 40])
    # 말의 좌표는 (board의 숫자, idx)
    horse = [[0, 0], [0, 0], [0, 0], [0, 0]]

    def move(org_horse, score, cnt):
        global max_score
        if cnt == 10:
            if score > max_score:
                max_score = score
            return
        # 파란색 -> 지름길
        # 빨간색 -> 그냥 직진
        for i in range(4):
            # 말이 도착칸에 있을 경우
            if org_horse[i][1] > 100:
                continue
            # 여기서 리스트를 카피
            horse = copy.deepcopy(org_horse)
            b, idx = horse[i]
            new_idx = idx + dice[cnt]

            # 말이 움직임, 해당 보드에서만 이동
            if b == 0:
                if new_idx >= 21:
                    horse[i] = [0, 1e4]
                    move(horse, score, cnt + 1)
                    continue
                # 끝나는 지점이 바뀌어야한다면 그때 바꿈
                else:
                    if new_idx == 20:
                        if [1, 7] in horse:
                            continue
                        if [2, 6] in horse:
                            continue
                        if [3, 7] in horse:
                            continue
                        if [0, 20] in horse:
                            continue
                        horse[i] = [0, 20]
                    elif new_idx == 5:
                        if [1, 0] in horse:
                            continue
                        horse[i] = [1, 0]
                    elif new_idx == 10:
                        if [2, 0] in horse:
                            continue
                        horse[i] = [2, 0]
                    elif new_idx == 15:
                        if [3, 0] in horse:
                            continue
                        horse[i] = [3, 0]
                    else:
                        if [0, new_idx] in horse:
                            continue
                        horse[i] = [0, new_idx]
                    move(horse, score + board[0][new_idx], cnt + 1)

            elif b == 1 or b == 3:
                if new_idx >= 8:
                    horse[i] = [b, 1e4]
                    move(horse, score, cnt + 1)
                    continue

                else:
                    if new_idx == 7:
                        if [1, 7] in horse:
                            continue
                        if [2, 6] in horse:
                            continue
                        if [3, 7] in horse:
                            continue
                        if [0, 20] in horse:
                            continue
                    elif new_idx >= 4:
                        if [1, new_idx] in horse:
                            continue
                        if [2, new_idx - 1] in horse:
                            continue
                        if [3, new_idx] in horse:
                            continue
                    horse[i] = [b, new_idx]
                    move(horse, score + board[b][new_idx], cnt + 1)

            else:
                if new_idx >= 7:
                    horse[i] = [b, 1e4]
                    move(horse, score, cnt + 1)
                    continue
                else:
                    if new_idx == 6:
                        if [1, 7] in horse:
                            continue
                        if [2, 6] in horse:
                            continue
                        if [3, 7] in horse:
                            continue
                        if [0, 20] in horse:
                            continue
                    elif new_idx >= 3:
                        if [1, new_idx + 1] in horse:
                            continue
                        if [2, new_idx] in horse:
                            continue
                        if [3, new_idx + 1] in horse:
                            continue
                    horse[i] = [b, new_idx]
                    move(horse, score + board[b][new_idx], cnt + 1)

    move(copy.deepcopy(horse), 0, 0)
    print(max_score)


if __name__ == "__main__":
    main()
