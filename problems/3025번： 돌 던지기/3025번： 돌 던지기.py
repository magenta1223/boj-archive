#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3025                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3025                          #+#        #+#      #+#     #
#     Solved: 2024-07-08 02:27:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 시뮬레이션인데 빠르게 해야 함 

# 1. 돌 아랫칸이 벽 / 가장 아래면 -> 그자리에 그대로
# 2. 비어있으면 -> 아래로 
# 3. 돌이면 
# 3-1) 왼쪽/왼쪽 아래가 비었으면 -> 왼쪽으로 미끄러진다 
# 3-2) 오른쪽/오른쪽 아래가 비었으면 -> 오른쪽 
# 3-3) 다 차있으면 -> 멈춰! 

# 열과 현재 높이가 주어지면
# 현재 높이 이하에서 다음과 같은 로직을 수행 
# 1. 가장 가까운 벽을 찾는다 -> 있다면 그 위에 쌓이고
# 2. 가장 가까운 돌을 찾는다 -> 그 위치를 찾고 수행 

# 10만개가 한곳에 떨어져봐야 높이는 최대 1000 
# 열 별로 바닥, 벽을 아래서부터 순서대로 만들어 놓고 
# 그 열로 떨어지면 -> 현재 높이 이하에 있으면서 마지막 벽/바닥에서 가장 높은 바위를 찾고
# 로직에 따라 처리


input = open(0).readline  
R,C = map(int,input().split())
A = [list(input().strip()) for _ in range(R)]
N = int(input())
STONES = [int(input())-1 for _ in range(N)]

# 어떤 열에서 떨어지면 -> 특정 위치까지 shortcut을 따라가고 거기서 시뮬레이션 수행 
# shortcut 업데이트 

def fall(x,y,c):
    while True:
        shortcuts[c].append((x,y))
        if x+1 == R or A[x+1][y] == "X":
            A[x][y] = "O"
            return 
        elif A[x+1][y] == "O":
            if y and A[x][y-1] == "." and A[x+1][y-1] == ".":
                y -= 1
            elif y < C-1 and A[x][y+1] == "." and A[x+1][y+1] == ".":
                y += 1 
            else:
                A[x][y] = "O"
                return
        x += 1 
    
shortcuts = [[] for _ in range(C)]

for s in STONES:
    while shortcuts[s]:
        x,y = shortcuts[s][-1]
        if A[x][y] == ".":
            break 
        shortcuts[s].pop()

    if shortcuts[s]:
        x,y = shortcuts[s][-1]
    else:
        x,y = 0,s 

    fall(x,y,s)

print(*["".join(row) for row in A], sep = '\n')