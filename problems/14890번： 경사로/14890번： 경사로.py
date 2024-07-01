#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14890                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14890                         #+#        #+#      #+#     #
#     Solved: 2024-02-13 14:48:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,L=map(int,input().split())
BOARD=[list(map(int,input().split())) for _ in range(N)]
FLIPPED=[list(row) for row in zip(*BOARD)]
# 행 / 열에 대해 순회
# 단차가 2이상 -> 죽어 
# 1 -> 경사로를 놓을 수 있는지 체크
# 현재 - 다음 이 음수 -> 오른쪽으로
# 양수 -> 왼쪽으로 
# 끝에 무사히 도달하면 가능 ! 
 
def check(row):
    tilt = [False] * N
    for i in range(N-1):
        diff = row[i] - row[i+1]
        if diff == 0:
            continue 
        elif diff > 1 or diff < -1:
            return 0 
        elif diff == 1: # toward right 
            for j in range(1,L+1):
                if i+j >= N or row[i+j] != row[i+1] or tilt[i+j]:
                    return 0 
            tilt[i+1:i+L+1] = [True] * L
        else: # toward left 
            for j in range(L): 
                if i-j < 0 or row[i-j] != row[i] or tilt[i-j]:
                    return 0 
            tilt[i-L+1:i+1] =  [True] * L
    return 1
 
print(  sum([check(row) for row in BOARD]) + sum([check(row) for row in FLIPPED]))