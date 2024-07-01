#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17779                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17779                         #+#        #+#      #+#     #
#     Solved: 2024-02-19 12:36:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def color(board, range_x, range_y, num):
    for i in range(*range_x):
        for j in range(*range_y):
            board[i][j] = num
    return board 
 
def populations_range(array, board):
    l = [0] * 5
    for i in range(N):
        for j in range(N):
            l[board[i][j]] += array[i][j]
    return max(l) - min(l)
 
N=int(input().strip())
A=[list(map(int,input().split())) for _ in range(N)]
impossible_points = [(0,0), (0,N-1), (N-1,0), (N-1,N-1)]
 
 
 
ans = float("inf")
 
for x in range(N):
    for y in range(N):
        if (x,y) in impossible_points:
            continue
        B = [[0] * N for _ in range(N)]
        for d1 in range(1, y+1):
            for d2 in range(1, min(N-y, N-x-d1)):
                ranges_x = [(0,x+d1), (0,x+d2+1), (x+d1, N), (x+d2+1,N)]
                ranges_y = [(0,y+1), (y+1, N), (0, y-d1+d2), (y-d1+d2, N)]
                # 1~4
                for i, (range_x, range_y) in enumerate(zip(ranges_x, ranges_y)):
                    B = color(B, range_x, range_y, i)
                for i in range(x, x+d1+d2+1):
                    cmin = y+x-i if i-x <= d1 else y+i-x-2*d1
                    cmax=y+i-x+1 if i-x <= d2 else y-i+2*d2+x+1
                    for j in range(cmin, cmax):
                        B[i][j] = 4
                res = populations_range(A, B)
                if res < ans:
                    ans = res
print(ans)