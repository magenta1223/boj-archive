#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14888                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14888                         #+#        #+#      #+#     #
#     Solved: 2023-12-18 18:25:48 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
l = list(map(int, input().split()))
pl, mi, mul, div = map(int, input().split())
 
 
def divide(a, b):
    if a < 0 and b > 0:
        return - ((-a) // b)
    else:
        return a // b
 
results = []
visited = []
def dfs(result, depth):
    global pl, mi, mul, div
    if depth == N:
        results.append(result)
    else:
        if pl:
            pl -=1 
            dfs(result + l[depth], depth+1)
            pl += 1
        if mi:
            mi -=1 
            dfs(result - l[depth], depth+1)
            mi += 1
        if mul:
            mul -=1 
            dfs(result * l[depth], depth+1)
            mul += 1
        if div:
            div -=1 
            dfs(divide(result, l[depth]), depth+1)
            div += 1
        
dfs(result=l[0], depth = 1)
print(max(results))
print(min(results))