#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5373                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5373                          #+#        #+#      #+#     #
#     Solved: 2024-02-26 14:42:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from copy import deepcopy
N = 3
def rotate(side):
    tmp = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[j][N-i-1] = side[i][j]
    return tmp 
C = {'U' : 'w', 'D' : 'y', 'F' : 'r', 'B' : 'o', 'L' : 'g', 'R' : 'b',}
LOCS = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
class Cube:
    def __init__(self) -> None:
        self.sides = { side : [[fill] * N for _ in range(N)] for side, fill in C.items()}
        #   U
        # L F R B
        #   D
        self.targets = {
            'U' : {
                'targets' : [('B'), ('R'), ('F'), ('L')],
                'locs' : [(0,1,2), (0,1,2), (0,1,2),(0,1,2)], 
            },            
            'D' : {
                'targets' : [('L'), ('F'), ('R'), ('B')],
                'locs' : [(6,7,8), (6,7,8), (6,7,8),(6,7,8)], 
            },
            'F' : {
                'targets' : [('L'), ('U'), ('R'), ('D')],
                'locs' : [(2,5,8), (8,7,6), (6,3,0),(0,1,2)], 
            },
            'B' : {
                'targets' : [('D'), ('R'), ('U'), ('L')],
                'locs' : [(6,7,8), (8,5,2), (2,1,0),(0,3,6)], 
            },
            'L' : {
                'targets' : [('U'), ('F'), ('D'), ('B')],
                'locs' : [(0,3,6), (0,3,6), (0,3,6),(8,5,2)], 
            },
            'R' : {
                'targets' : [('D'), ('F'), ('U'), ('B')],
                'locs' : [(2,5,8), (2,5,8), (2,5,8),(6,3,0)], 
            },
        }
    
    def rotate(self, command):
        side, clockwise = command
        self._rotate(side)
        if clockwise == "-":
            self._rotate(side)
            self._rotate(side)
    def _rotate(self, side):
        targets, locs = self.targets[side]['targets'], self.targets[side]['locs']
        copied = {t : deepcopy(self.sides[t]) for t in targets}
        for side_idx in range(4):
            s, ns = targets[side_idx], targets[(side_idx+1)%4]
            ls, nls = locs[side_idx], locs[(side_idx+1)%4]
            for l, nl in zip(ls, nls):
                x,y = LOCS[l]
                px,py = LOCS[nl]
                copied[ns][px][py] = self.sides[s][x][y]
        for k in copied.keys():
            self.sides[k] = copied[k]
        self.sides[side] = rotate(self.sides[side])
 
T=int(input().strip())
for _ in range(T):
    n=int(input().strip())
    cube = Cube()
    commands = input().split()
    for command in commands:
        cube.rotate(command)
    for row in cube.sides['U']:
        print("".join(row))
 