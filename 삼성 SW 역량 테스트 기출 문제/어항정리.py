# 어항정리
def main():
    # 2차원 리스트: 행렬로만 들어가야함!
    def rotate_matrix(matrix):
        rows, cols = len(matrix), len(matrix[0])
        # 회전된 행렬 초기화 (가로와 세로 길이가 바뀜)
        rotated_matrix = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated_matrix[j][rows - 1 - i] = matrix[i][j]
        return rotated_matrix

    # 불가능할 때: 공중부양하는 matrix의 가로 세로 길이만큼 바닥이 존재하지 않을 때
    def levitate1(matrix, cnt):
        if cnt == 1:
            tmp_lst = [matrix[:1], matrix[1:2]]
            rotate_lst = rotate_matrix(tmp_lst)
            rotate_lst.append(matrix[2:])
        else:
            if len(matrix[-1]) < cnt + len(matrix):
                return matrix
            tmp_lst = matrix[:-1]
            tmp_lst.append(matrix[-1][:cnt])
            rotate_lst = rotate_matrix(tmp_lst)
            rotate_lst.append(matrix[-1][cnt:])
        # 재귀함수에 리턴값을 반드시 줘야함!!
        return levitate1(rotate_lst, len(rotate_lst[0]))

    def adjust_fish(matrix):
        rows, cols = len(matrix), len(matrix[-1])
        # 오른쪽, 아래 방향으로만 진행
        dx, dy = [-1, 0], [0, 1]
        # 행렬 초기화
        change = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(len(matrix[i])):
                for idx in range(2):
                    nx, ny = i + dx[idx], j + dy[idx]
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[nx]):
                        # print(i,j, nx,ny, matrix[i][j], matrix[nx][ny])
                        if matrix[i][j] >= matrix[nx][ny]:
                            change[nx][ny] += (matrix[i][j] - matrix[nx][ny]) // 5
                            change[i][j] -= (matrix[i][j] - matrix[nx][ny]) // 5
                        else:
                            change[i][j] += (matrix[nx][ny] - matrix[i][j]) // 5
                            change[nx][ny] -= (matrix[nx][ny] - matrix[i][j]) // 5
        for i in range(rows):
            for j in range(len(matrix[i])):
                matrix[i][j] += int(change[i][j])
        return matrix

    def make_linear(matrix):
        rows, cols = len(matrix), len(matrix[-1])
        linear_lst = []
        for i in range(cols):
            for j in range(rows - 1, -1, -1):
                if j < 0 or j >= len(matrix) or i < 0 or i >= len(matrix[j]):
                    continue
                linear_lst.append(matrix[j][i])
        return linear_lst

    def levitate2(matrix):
        N = len(matrix)
        slice1 = N // 2
        levitate2_lst = []
        levitate2_lst.append((matrix[:slice1][::-1]))
        levitate2_lst.append(matrix[slice1:])
        slice2 = len(levitate2_lst[-1]) // 2

        levitate2_matrix = rotate_matrix(
            rotate_matrix([row[:slice2] for row in levitate2_lst])
        )
        for i in levitate2_lst:
            levitate2_matrix.append(i[slice2:])
        return levitate2_matrix

    def cleaning(first_lst, total_cnt):
        # 최대 - 최소가 k 이하일때 종료
        if (max(first_lst) - min(first_lst)) <= K:
            return total_cnt
        # 가장 작은 어항에 물고기 +1
        c = min(first_lst)
        for i in range(len(first_lst)):
            if first_lst[i] == c:
                first_lst[i] += 1
        levitate1_lst = levitate1(first_lst, 1)
        adjust1_lst = adjust_fish(levitate1_lst)
        linear1_lst = make_linear(adjust1_lst)
        levitate2_lst = levitate2(linear1_lst)
        adjust2_lst = adjust_fish(levitate2_lst)
        linear2_lst = make_linear(adjust2_lst)
        return cleaning(linear2_lst, total_cnt + 1)

    print(cleaning(lst, 0))


if __name__ == "__main__":
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    main()