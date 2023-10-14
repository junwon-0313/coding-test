def main():
    def combinations(array, r):
        for i in range(len(array)):
            if r==1:
                yield [array[i]]
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next
    def sub_set(array):
        sub_lst = []
        for i in range(len(array)):
            for j in list(combinations(array,i+1)):
                sub_lst.append(sum(j)/len(j))
        return sub_lst
    T = int(input())
    for t in range(T):
        n = int(input())
        S = list(map(int,input().split()))

        # 공집합이 아닌 부분집합의 평균을 구하고
        sub_l = sub_set(S)
        # 평균의 평균을 구한다.
        # 소수점 20번째 자리에서 출력한다.
        result = sum(sub_l)/len(sub_l)
        if result == sum(sub_l)//len(sub_l):
            print(f'#{t+1} {int(result)}')
        else:
            print(f'#{t+1} {round(result,20)}')

if __name__=='__main__':
    main()
