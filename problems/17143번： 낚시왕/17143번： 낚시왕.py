#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17143                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17143                         #+#        #+#      #+#     #
#     Solved: 2024-02-18 16:54:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

isOdd = lambda x:  True if x % 2 else False
 
class Shark:
    def __init__(self, r,c,s,d,z):
        self.r = r
        self.c = c
        self.s = s 
        self.d = d 
        self.z = z 
    
    def __repr__(self):
        return f"Shark at {self.r+1}, {self.c+1} with size {self.z}, D : {self.d}"
        
    def move(self):
        s = self.s
        dr, dc = self.d 
        r, c = self.r+1, self.c+1 
        nr, nc = r+s*dr, c+s*dc
        while not (0<nr<=R and 0<nc<=C):
            # 3.1 
            if nr <= 0:
                nr = -nr+2
                dr *= -1
            elif nr > R:
                nr = 2*R - nr
                dr *= -1
            if nc <= 0:
                nc = -nc+2 # 
                dc *= -1
            elif nc > C:
                nc = 2*C - nc
                dc *= -1
        self.r, self.c = nr - 1, nc -1
        self.d = dr, dc 
    
def fight(sharks):
    z = 0
    for shark in sharks:
        if shark.z > z:
            biggest = shark
            z = biggest.z
    return biggest 
 
R,C,M=map(int,input().split())
BOARD = [[0] * C for _ in range(R)]
D = {
    1 : (-1,0),
    2 : (1,0),
    3 : (0,1),
    4 : (0,-1)
}
 
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    r-=1
    c-=1
    d = D[d]
    BOARD[r][c] = Shark(r,c,s,d,z)
    
    
    
# 1. 오른쪽으로 한칸 이동 
# 2. 
    # 1) 낚시왕이 있는 열에 있는 상어 중 땅과 가까운 상어를 잡음. 
    # 2) 잡으면 상어가 사라지고
# 3. 상어가 이동 
    # 1) 이동 시 벽에 부딫히면 반대로 
    # 2) 겹치면 더 큰 상어가 남음 
 
ans = 0
for king_c in range(C):
    # 1. 
    for r in range(R):
        # 2. 
        if BOARD[r][king_c]:
            shark = BOARD[r][king_c]
            # 2.1
            ans += shark.z
            # 2.2
            BOARD[r][king_c] = 0
            break 
    nextBOARD = [[0] * C for _ in range(R)]
    # 3.  
    for r in range(R):
        for c in range(C):
            if BOARD[r][c]:
                shark = BOARD[r][c]
                shark.move()
                nr, nc = shark.r, shark.c
                # 3.2
                if nextBOARD[nr][nc]:
                    shark = fight([nextBOARD[nr][nc], shark])
                nextBOARD[nr][nc] = shark 
    BOARD = nextBOARD
print(ans)