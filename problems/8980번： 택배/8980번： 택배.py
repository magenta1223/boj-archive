#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 8980                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/8980                          #+#        #+#      #+#     #
#     Solved: 2024-05-23 11:30:32 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,C=map(int,input().split())
M=int(input())
l = [list(map(int,input().split())) for _ in range(M)]
# 도착지 순 정렬 
l.sort(key = lambda x: x[1])
 
# 각 마을에서 사용 가능한 트럭 용량 
available = [C]*N 
ans = 0 
 
for s,e,box in l:
    tmp = C 
    # 이 택배를 차에 전부 실으려면 구간 내 용량이 전부 box 이상이어야 함
    # 택배의 시작~도착이 가능한 양만큼 싣는다. (일부만 싣기 가능) 
    tmp = min(available[s:e] + [C, box])
    for i in range(s,e):
        available[i] -= tmp # tmp만큼 택배를 실었으니 그 사이에는 tmp만큼 용량이 깎임. 
    ans += tmp 
print(ans)