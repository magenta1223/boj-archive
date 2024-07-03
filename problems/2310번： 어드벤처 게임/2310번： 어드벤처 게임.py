#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2310                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2310                          #+#        #+#      #+#     #
#     Solved: 2024-07-03 09:35:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from heapq import * 
INF = float("inf")

while True:
    N = int(input())
    if not N:
        break 
    
    G = {i: [] for i in range(1,N+1)}
    Rooms = {i: [] for i in range(1,N+1)}
    for i in range(1,N+1):
        Room = input().split()
        t,v,dests = Room[0], Room[1], Room[2:-1]
        Rooms[i] = t,int(v) 
        for d in dests:
            G[i].append(int(d))
    v = 0
    t,m = Rooms[1]
    if t == "L":
        v += m
    else:
        v -= m
    
    if v < 0:
        print("No")
        continue 

    heap = [(-v,1)]
    costs = [-INF]* (N+1)
    costs[1] = v
    # 돈을 남기는게 중요하니 최대비용으로 방문해보자 

    while heap:
        money, now = heappop(heap)
        money *= -1
        for next in G[now]:
            if Rooms[next][0] == "E":
                nextMoney = money
            elif Rooms[next][0] == "L":
                nextMoney = max(money, Rooms[next][1])
            else:
                nextMoney = money - Rooms[next][1]
            if nextMoney >= 0 and costs[next] < nextMoney:
                costs[next] = nextMoney
                heappush(heap, (-nextMoney, next))
    print("Yes" if costs[-1] != -INF else "No")


    
