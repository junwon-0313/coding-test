def main():
    def rotate():
        end = durability_lst[-1]
        durability_lst[1:] = durability_lst[0:-1]
        durability_lst[0] = end
        for i in range(len(robots)):
            robots[i]+=1

    def drop():
        if len(robots)==0:
            return
        if robots[0]==N-1:
            robots.pop(0)

    def move_robot():
        # 로봇 리스트 중 맨 앞부터 한칸 갈 수 있다면, 내구성 테스트+ 앞에 로봇이 없는지
        for i in range(len(robots)):
            idx = robots[i]+1
            if durability_lst[idx]>=1 and idx not in robots:
                robots[i]+=1
                durability_lst[idx]-=1

    def load():
        if durability_lst[0] >=1:
            durability_lst[0]-=1
            robots.append(0)


    N,K = map(int,input().split())
    # 전역 변수
    durability_lst = list(map(int,input().split()))
    robots = []
    count=0
    while True:
        count+=1
        rotate()
        drop()
        move_robot()
        drop()
        load()
        if durability_lst.count(0)>=K:
            break
    print(count)

if __name__=='__main__':
    main()
