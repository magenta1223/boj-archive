#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 27651                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/27651                         #+#        #+#      #+#     #
#     Solved: 2024-06-04 12:02:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
N = int(input())
A = list(map(int, input().split()))
 
SUM = [A[i] for i in range(N)]
for i in range(1,N):
    SUM[i] += SUM[i-1]
 
 
def part_sum(a, b):
    if a == 0:
        return SUM[b]
    return SUM[b] - SUM[a-1]
 
 
res = 0
bae = N-1
momtong = 2
for head_idx in range(1, N-1):
    head = SUM[head_idx-1]
    
    # 머리 < 배
    while head >= part_sum(bae, N-1):
        bae -= 1
 
    while part_sum(head_idx, momtong-1) <= part_sum(momtong, N-1):
        momtong += 1
 
    if momtong <= bae and momtong < N:
        res += (bae - momtong + 1)
    else: 
        break
 
print(res)