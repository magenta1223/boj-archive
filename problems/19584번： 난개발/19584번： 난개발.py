#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 19584                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/19584                         #+#        #+#      #+#     #
#     Solved: 2024-07-19 03:46:59 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline

N,M = map(int,input().split())
A = [list(map(int,input().split()))[1] for _ in range(N)]

# 좌표 압축 
comp = {a:i for i,a in enumerate(sorted(set(A)))}
A = [comp[a] for a in A]
mx = max(A)

arr = [0] * (mx+1)
diff = [0] * (mx + 2)  

for _ in range(M):
    u,v,c = map(int,input().split())
    a,b = A[u-1], A[v-1]
    a,b = min(a,b), max(a,b)
    diff[a] += c 
    diff[b+1] -= c 


for i in range(mx+1):
    arr[i] += arr[i-1] + diff[i]

print(max(arr))    
