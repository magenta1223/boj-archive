#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1079                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1079                          #+#        #+#      #+#     #
#     Solved: 2024-09-23 07:04:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 유일한 마피아로 안죽고 최대한 많은 밤을 버티기
# dp로 풀면 안됨. 완전탐색. 
# 밤에만 유죄가 바뀌기 때문에 밤에죽은 사람과 낮에죽은 사람을 별도로 관리해야 함. 
# 즉, 밤에죽은 mask * 낮에죽은 bitmask의 경우를 전부 고려
# 2^32 -> 멤초 

N = int(input())
Guilty = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
EJ = int(input())
isAlive = [1] * N 

def dfs(i, left, isDay):
    if i==EJ or left == 1:
        return 0
    # 낮인가? 밤인가? 
    if isDay:
        maxGuilty = -1 
        for p in range(N):
            if isAlive[p]:
                if Guilty[p] > maxGuilty:
                    maxGuilty, die = Guilty[p], p
        isAlive[die] = 0 
        res = dfs(die, left-1, 0)
        isAlive[die] = 1
        return res

    else:
        res = 0 
        for p in range(N):
            if not isAlive[p] or p == EJ:
                continue 
            for _p in range(N):
                Guilty[_p] += R[p][_p]
            isAlive[p] = 0
            res = max(res, dfs(p, left-1, 1)+1) 
            for _p in range(N):
                Guilty[_p] -= R[p][_p]
            isAlive[p] = 1 
    return res 

print(dfs(-1,N,N%2))

