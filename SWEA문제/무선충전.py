T = int(input())
for t in range(T):
    # 좌표 1~10
    m, a = map(int,input().split())
    battery = [] # 좌표,범위, 파워
    user1 = list(map(int,input().split()))
    user2 = list(map(int,input().split()))
    for _ in range(a):
        battery.append(list(map(int,input().split())))

    dxs, dys = [0,0,1,0,-1], [0,-1,0,1,0]
    pos1 = (1,1)
    pos2 = (10,10)

    total_power = 0

    def distance(start, end):
        return abs(start[0]-end[0])+abs(start[1]-end[1])

    # 0초일 때 배터리 충전 -> 제자리 이동
    user1.insert(0,0)
    user2.insert(0,0)

    for d in range(m+1): # 1초 ~m초
        # print('Time',d)
        # print(total_power)
        # 이동 후
        pos1 = (pos1[0]+dxs[user1[d]], pos1[1]+dys[user1[d]])
        pos2 = (pos2[0]+dxs[user2[d]], pos2[1]+dys[user2[d]])
        # 사용가능한 배터리 찾기
        b1 = []
        b2 = []
        for idx in range(a):
            bx, by, c, p = battery[idx]
            if distance(pos1, (bx,by))<=c:
                b1.append((idx,p))
            if distance(pos2, (bx,by))<=c:
                b2.append((idx,p))
        # 배터리 충전
        b1.sort(key=lambda x:-x[1])
        b2.sort(key=lambda x:-x[1])
        # print('@@@')
        # print(b1)
        # print(b2)
        if len(b1)==0 and len(b2)==0:
            continue
        elif len(b1)==0:
            total_power += b2[0][1]
            continue
        elif len(b2)==0:
            total_power += b1[0][1]
            continue

        if b1[0]==b2[0]:
            total_power += b1[0][1]
            if len(b1)==1 and len(b1)==len(b2):
                continue
            elif len(b1)==1:
                total_power+=b2[1][1]
            elif len(b2)==1:
                total_power+=b1[1][1]
            else:
                total_power+=max(b1[1][1], b2[1][1])
        else:
            total_power += b1[0][1]
            total_power += b2[0][1]


    print(f'#{t+1} {total_power}')





