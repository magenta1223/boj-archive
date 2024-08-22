#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3955                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3955                          #+#        #+#      #+#     #
#     Solved: 2024-08-20 00:12:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 사탕을 나눠준다. 
# K명이 참가하면 K*X+1개를 준비 
# 사탕은 봉지단위로 판매함. 한 봉지에는 C개가 들어있다.
# 몇 봉지를 사야하지? 



from math import gcd 
input = open(0).readline 
def EEA(r1:int, r2:int):
    s1,s2 = 1,0
    t1,t2 = 0,1 
    while r2:
        q = r1//r2 
        r = r1 - q*r2
        r1,r2 = r2, r 
        s1,s2 = s2, s1-q*s2 
        t1,t2 = t2, t1-q*t2
    return s1

MAX = 10**9

for _ in range(int(input())):
    K,C =  map(int, input().split())

    if K==1:
        print(2 if C==1 else 1)
        continue 
    if C==1:
        print(K+1 if K < MAX else "IMPOSSIBLE")
        continue

    _gcd = gcd(K,C)
    if _gcd != 1:
        print("IMPOSSIBLE")
        continue
    
    ans = EEA(C,K)

    if ans > MAX:
        print("IMPOSSIBLE")

    print(ans if ans > 0 else K+ans)




"""
5
10 5
10 7
1337 23
123454321 42
999999937 999999939

"""