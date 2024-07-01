#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14503                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14503                         #+#        #+#      #+#     #
#     Solved: 2024-02-12 15:45:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 1. 현재 칸이 먼지 -> 청소
# 2. 주변 빈칸이 모두 청소됨. 
#    2-1) 바라보는 방향 유지한 상태로 한칸 후진 가능한지? -> 후진하고 1번 
#    2-2) 후진 못하면 -> 멈춤
# 3. 안청소된 빈칸 있다면
#    3-1 ) 반시계 방향으로 90도 회전
#    3-2 ) 바라보는 방향 기준 앞쪽 칸이 청소되지 않았다면 한칸 전진 
class Cleaner:
    def __init__(self, position, direction, room):
        self.x, self.y = position
        self.direction = direction
        self.room = room
        self.toward = [[-1, 0], [0, 1], [1, 0], [0,-1]]
        self.backward = [[1, 0], [0, -1], [-1, 0], [0,1]]
        self.results = {
            0 : "dust",
            1 : "wall",
            2 : "done"
        }
        
    def change_dir(self):
        # 북 0 동 1 남 2 서 3
        # 북 -> 서 -> 남 -> 동 순 
        self.direction = self.direction - 1 if self.direction else 3 
    def check_and_move(self):
        # 3
        for _ in range(4):
            # 3.1 
            self.change_dir()
            
            # 3.2
            dx, dy = self.toward[self.direction]
            if 0<=self.x+dx<N and 0<=self.y+dy<M:
                result = self.results[self.room[self.x+dx][self.y+dy]]
            else:
                result = "room_outside"
            if result == "dust":
                self.x += dx
                self.y += dy
                return # keep going
        # 2
        dx, dy = self.backward[self.direction]
        if 0<=self.x+dx<N and 0<=self.y+dy<M and self.room[self.x+dx][self.y+dy] != 1:
            self.x+=dx
            self.y+=dy
            return # keep going 
        else:
            return "end" # end 
    def clean(self):
        if self.room[self.x][self.y] == 0: # dust
            self.room[self.x][self.y] = 2 # done
            return 1 
        else:
            return 0
        
    def solve(self):
        res = None
        ans = 0
        while res != "end":
            # 1.
            ans += self.clean()
            # 2,3
            res = self.check_and_move()
        print(ans)
N,M=map(int, input().split())
x,y,d=map(int,input().split())
ROOM=[list(map(int,input().split())) for _ in range(N)]
cleaner=Cleaner((x,y),d,ROOM)
cleaner.solve()