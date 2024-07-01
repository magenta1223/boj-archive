#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11724                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11724                         #+#        #+#      #+#     #
#     Solved: 2024-03-05 00:38:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int,input().split())
unf = [i for i in range(N+1)]
def find(a):
    if unf[a] == a:
        return a 
    unf[a] = find(unf[a])
    return unf[a]
 
def union(a,b):
    a,b=find(a), find(b)
    unf[b] = a
 
for _ in range(M):
    union(*map(int,input().split()))
 
for i in range(1,N+1):
    find(i)
    
print(len(set(unf[1:])))