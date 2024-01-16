def main():
    dice = list(map(int, input().split()))
    lst = []
    for i in range(1, 7):
        lst.append((i, dice.count(i)))
    lst = sorted(lst, key=lambda x: (-x[1], -x[0]))
    max_num, cnt = lst[0]
    if cnt == 3:
        print(10000 + max_num * 1000)
    elif cnt == 2:
        print(1000 + max_num * 100)
    else:
        print(max_num * 100)


if __name__ == "__main__":
    main()
