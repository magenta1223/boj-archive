#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 8972                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/8972                          #+#        #+#      #+#     #
#     Solved: 2024-05-20 14:08:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input= open(0).readline
 
N,M = map(int,input().split())
A = [list(input().strip()) for _ in range(N)]
S=input().strip()
 
MADS = []
for i in range(N):
    for j in range(M):
        if A[i][j] == "I":
            x,y= i,j
        elif A[i][j] == "R":
            MADS.append((i,j))
            
D=[(0,0),(1,-1),(1,0),(1,1),(0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1)]
 
def find(x,y,mx,my):
    mx += 1 if x>mx else (-1 if x<mx else 0)
    my += 1 if y>my else (-1 if y<my else 0)
    return mx,my
 
done = False 
for i in range(len(S)):
    dx,dy = D[int(S[i])]
    # 1. 종두이노 
    x,y = x+dx, y+dy
    # 2. 미두이노와 만났나요 
    if (x,y) in MADS:
        done = True 
        break 
    
    # 3. 미두이노 움직이기 
    for j in range(len(MADS)):
        MADS[j] = find(x,y,*MADS[j])
        # 3-1) 미두이노와 종두이노가 만났는지 
        if (x,y) == MADS[j]:
            done = True 
            break 
    
    # 4. 겹치는 미두이노 지우기 
    dels = []
    for j in range(len(MADS)):
        if MADS.count(MADS[j]) > 1:
            dels.append(j)
 
    for d in dels[::-1]:
        del MADS[d]
    if done:
        break 
 
 
if done:
    print("kraj", i+1)
else:
    A = [["."] * M for _ in range(N)]
    A[x][y] = "I"
    for x,y in MADS:
        A[x][y] = "R"
 
    print(*["".join(line) for line in A], sep ='\n')