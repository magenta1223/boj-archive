#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4195                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4195                          #+#        #+#      #+#     #
#     Solved: 2024-03-13 15:28:32 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
def find(a):
    pa = parent[a]
    if pa == a:
        return a 
    parent[a] = find(pa)
    return parent[a]
 
def union(a, b):
    parent[b] = a
    cnt[a] += cnt[b]
 
for _ in range(int(input())):
    F = [input().split() for _ in range(int(input()))]
    people = set()
    [people.update(rel) for rel in F]
    people = list(people)
    parent = [i for i in range(len(people))]
    ptoi = {people[i] : i for i in range(len(people))} # person to index 
    cnt = [1 for _ in range(len(people))]
 
    for a, b in F:        
        a, b = ptoi[a], ptoi[b]
        if a > b:
            a,b = b,a 
        a,b = find(a), find(b)
        if a != b: # 반드시 find로 할 것 
            union(a,b)
        print(cnt[a])