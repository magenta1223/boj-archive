#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1043                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1043                          #+#        #+#      #+#     #
#     Solved: 2024-03-06 11:34:54 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int,input().split())
TRUTH = list(map(int,input().split()))[1:]
PARTIES = [list(map(int,input().split()))[1:] for _ in range(M)]
 
parent = [i for i in range(N+1)]
 
def find(a):
    if parent[a] == a:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
def union(a, b):
    a,b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
 
for t in TRUTH:
    parent[t] = 0
 
for party in PARTIES:
    a = party[0]
    for attendee in party[1:]:
        union(a, attendee)
        
# for i in range(N):
#     find(i)
    
print(sum([all([find(a) != 0 for a in party]) for party in PARTIES]))