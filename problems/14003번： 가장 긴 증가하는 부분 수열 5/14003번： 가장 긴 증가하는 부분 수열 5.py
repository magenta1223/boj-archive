#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14003                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14003                         #+#        #+#      #+#     #
#     Solved: 2024-02-06 12:42:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from bisect import bisect_left
N=int(input())
L=list(map(int, input().split()))
tails = []
# tails[i] = 길이가 i+1인 lis의 마지막 원소의 최소값을 나타냄. 
# = tails는 lis가 아니다 대체 시 원래 자리에 있던 애들을 역추적해야 그게 lis 
indices = []
prev = [-1] * N
 
for i in range(N):
    l = L[i]    
    x = bisect_left(tails, l)
    if x == len(tails):
        tails.append(l)
        indices.append(i)
    else:
        tails[x] = l
        indices[x] = i
    if x > 0:
        prev[i] = indices[x-1]
        # prev[i]는 lis의 i-1번째 요소에 대한 값을 알려주기 위한 배열
 
lis = []
idx = indices[-1] # 가장 마지막 원소의 index
while idx != -1:
    lis.append(L[idx]) # 역으로 거슬러 올라가며 더함 
    idx = prev[idx] # 
lis.reverse()
                
print(len(tails))
print(*lis)