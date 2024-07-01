#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2066                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2066                          #+#        #+#      #+#     #
#     Solved: 2024-03-29 17:24:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

MAX = 9
toNum = {str(i) : i for i in range(6,10)}
for i, s in enumerate(['T', 'J', 'Q', 'K', 'A']):
    toNum[s] = i+1
GROUPS = [[ toNum[card[0]] for card in input().split()]  for _ in range(MAX)]
 
dp = dict()
def dfs(decks, prob):
    comb = tuple([len(deck) for deck in decks])
    
    # done 
    if not sum(comb):
        return prob
    # already visited 
    if comb in dp:
        return dp[comb] * prob
    # init 
    dp[comb] = 0
    # 
    candidates = []
    for i in range(MAX):
        for j in range(i+1, MAX):
            if decks[i] and decks[j] and decks[i][-1] == decks[j][-1]:
                candidates.append((i,j))
    
    # no candidates 
    if not candidates:
        dp[comb] = 0
        return 0 
    
    for i, j in candidates:
        a,b = decks[i].pop(), decks[j].pop()
        dp[comb] += dfs(decks, 1)
        decks[i].append(a)
        decks[j].append(b)
    dp[comb] *= prob * (1 / len(candidates))
    return dp[comb]
 
target = tuple([len(deck) for deck in GROUPS])
dfs(GROUPS, 1)
print(int(10**7 * dp[target]) / 10**7 )
 