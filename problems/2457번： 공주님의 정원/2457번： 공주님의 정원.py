#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2457                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2457                          #+#        #+#      #+#     #
#     Solved: 2024-05-23 13:56:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
N=int(input())
 
months = [31,28,31,30,31,30,31,31,30,31,30,31]
months2day = dict()
for i in range(1,14):
    months2day[i] = sum(months[:i-1])
 
 
S,E = months2day[3]+1, months2day[11] + 30
 
flowers = []
for _ in range(N):
    a,b,c,d = map(int,input().split())
    fa,fb = months2day[a]+b, months2day[c]+d
    if E<fa or fb<S:
        continue 
    flowers.append((a,b,c,d,fa,fb))
 
flowers.sort(key = lambda x:x[-1])
year = [0] * 366 
a,b,c,d,fa,fb = flowers[0]
for i in range(max(S,fa),fb):
    year[i] = 1 
 
s,e = fa,fb 
for a,b,c,d,fa,fb in flowers[1:]:
    # print(f"{a}월 {b}일 ~ {c}월 {d}일")  
    if e < fa:
        # print("공백 + 안겹")
        # 공백이 있는데 -> 다음에 와서 덮는다 -> 필요가 없음. 
        # 공백이 있는데 -> 다음에 못덮음 -> 어차피 안됨. 
        continue
    v = year[fa-1]
    for i in range(max(S,fa),fb):
        if year[i]:
            year[i] = min(v+1, year[i])
        else:
            year[i] = v+1
    s = min(s,fa)
    e = max(e,fb)
print(year[E] if year[S] else 0)