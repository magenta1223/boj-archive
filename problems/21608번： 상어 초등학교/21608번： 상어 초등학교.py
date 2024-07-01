#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 21608                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/21608                         #+#        #+#      #+#     #
#     Solved: 2024-02-22 11:20:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

D = [(-1,0),(1,0),(0,-1),(0,1)]
def search(idx):
    c = 0
    candidates = []
    for x in range(N):
        for y in range(N):
            n = 0
            _c = 0
            if not B[x][y]:
                for dx, dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<N and 0<=ny<N:
                        if B[nx][ny] in W[idx]:
                            _c += 1
                        elif not B[nx][ny]:
                            n += 1
                if _c > c:
                    c=_c
                    candidates = [(x,y,n)]
                elif _c == c:
                    candidates.append((x,y,n))
                
    candidates.sort(key=lambda x: (-x[2], x[0], x[1]))
    return candidates[0]
 
S={0:0, 1:1, 2:10, 3:100, 4:1000}
 
N=int(input().strip())
W = {}
B = [[0] * N for _ in range(N)]
i_s = []
for _ in range(N**2):
    i,a,b,c,d = map(int,input().split())
    W[i] = [a,b,c,d]
    x,y,_ = search(i)
    B[x][y] = i
    
ans = 0
for x in range(N):
    for y in range(N):
        i  = B[x][y]
        c = 0
        for dx, dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if B[nx][ny] in W[i]:
                    c += 1
        ans += S[c]
 
print(ans)
 