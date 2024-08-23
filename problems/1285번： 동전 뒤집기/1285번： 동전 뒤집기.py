#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1285                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1285                          #+#        #+#      #+#     #
#     Solved: 2024-08-23 07:22:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def str2num(row):
    num = 0
    for i in range(N):
        if row[i] == 'H':
            num += 1<<(N-i-1)
    return num 

def count_1(num):
    cnt = 0
    while num:
        cnt += num&1 
        num >>= 1
    return cnt 


N = int(input())
A = [str2num(input()) for _ in range(N)]
ans = N**2
for i in range(1<<N):
    res = 0
    for row in A:
        # 같은 mask에 대해 모든 행을 뒤집기 = 열을 뒤집는 모든 조합을 수행 
        cnt = count_1(row^i)
        # 이후 행을 뒤집어 T의 개수를 최소화 
        res += min(cnt, N-cnt)
    ans = min(res, ans)
print(ans)



    



"""
3
THT
HTH
THT

3
HHT
HHH
THT


4
HHTT
THTH
TTTH
TTHT

"""