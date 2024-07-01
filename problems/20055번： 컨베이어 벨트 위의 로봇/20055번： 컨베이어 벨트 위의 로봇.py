#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20055                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20055                         #+#        #+#      #+#     #
#     Solved: 2024-02-21 15:44:34 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
def check(conveyer):
    count = sum([ dur == 0 for dur, _ in conveyer])    
    return False if count >= K else True
 
N,K=map(int,input().split())
CONVEYER=list(map(int,input().split()))
CONVEYER = deque([(el, False) for el in CONVEYER])
 
t = 0
while check(CONVEYER):
    # 1. 한 칸 회전 
    CONVEYER.rotate(1)
    # 1) 회전하면서 내리기 
    dur, robot = CONVEYER[N-1]
    CONVEYER[N-1] = dur, False 
    # 2. 가장 먼저 올라간 로봇부터 한칸씩 이동 
    for i in range(N-2,-1,-1):
        # = 현재 칸 로봇이 없거나, 다음칸 내구도가 0이거나, 다음칸에 로봇이 있으면 안함
        dur, robot = CONVEYER[i]
        dur_next, robot_next = CONVEYER[i+1]
        if not robot or dur_next == 0 or robot_next:
            continue
        
        if i == N-2:
            # N-1에서 내림
            CONVEYER[i+1] = dur_next - 1, False
            CONVEYER[i]   = dur, False
        else:
            # 이동 
            CONVEYER[i+1] = dur_next - 1, robot
            CONVEYER[i]   = dur, False
    
    # 3. 로봇 올리기
    dur, _ = CONVEYER[0]
    if dur:
        CONVEYER[0] = dur-1, True
    t+=1
    
print(t)