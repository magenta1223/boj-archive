#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1050                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1050                          #+#        #+#      #+#     #
#     Solved: 2024-06-13 11:07:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(eq):
    price = 0
    for term in eq.split("+"):
        coef, var = term[0], term[1:]
        price += int(coef)*PRICES.get(var, INF)
    return price 
 
INF = float("inf")
N,M = map(int,input().split())
PRICES = dict()
for _ in range(N):
    ingredient, price = input().split()
    PRICES[ingredient] = int(price)
 
 
EQS = []
for _ in range(M):
    Eq = input()
    potion, eq = Eq.split("=")    
    EQS.append((potion, eq))
    PRICES[potion] = PRICES.get(potion, INF) 
 
 
for i in range(M):
    for j in range(M):
        potion, eq = EQS[j]
        PRICES[potion] = min(PRICES[potion], solve(eq))
 
ans = PRICES.get("LOVE", INF)
 
 
if ans == INF:
    print(-1)
elif ans > 1000000000:
    print(1000000001)
else:
    print(ans)