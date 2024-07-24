#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2233                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2233                          #+#        #+#      #+#     #
#     Solved: 2024-07-24 08:06:42 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N = int(input())
S = input()
X,Y = map(int,input().split())


G = [[] for _ in range(N+1)]
P = [0 for _ in range(N+1)]

node = 0 
node_idx = 0 

S2N = [-1 for _ in range(2*N)]
N2S = [[-1,-1] for _ in range(N+1)]
L = [0 for _ in range(N+1)]

for i in range(2*N):
    if S[i] == '0':
        node_idx += 1 
        G[node].append(node_idx)
        P[node_idx] = node 
        L[node_idx] = L[node] + 1 


        node = node_idx
        S2N[i] = node_idx
        N2S[node_idx][0] = i+1 

    else:
        N2S[node][1] = i+1 
        S2N[i] = node
        node = P[node]


X,Y = S2N[X-1], S2N[Y-1]

if L[X] > L[Y]:
    X,Y = Y,X 

while L[X] < L[Y]:
    Y = P[Y]

while X!=Y:
    X,Y = P[X], P[Y]

print(*N2S[X])