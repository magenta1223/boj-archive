#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17825                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17825                         #+#        #+#      #+#     #
#     Solved: 2024-02-20 13:15:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

L=list(map(int, input().split()))
 
G = {}
G[f'S0'] = {
    'red' : f'S1',
    'blue' : False,
    'value' : 0
}
for i in range(1,21):
    G[f'S{i}'] = {
        'red' : f'S{i+1}',
        'blue' : False,
        'value' : 2*i
    }
    if not i % 5:
        G[f'S{i}']['blue'] = f'C{i//5}1'
G['S20']['red'] = 'G'  
G['S20']['blue'] = False 
 
# 센터
for i in range(1,4):
    G[f'C1{i}'] = {
        'red' : f'C1{i+1}',
        'blue' : False,
        'value' : 10 + 3 * i
    }
G['C13']['red'] = 'C0' # center
 
for i in range(1,3):
    G[f'C2{i}'] = {
        'red' : f'C2{i+1}',
        'blue' : False,
        'value' : 20 + 2 * i
    }
G['C22']['red'] = 'C0' # center
 
for i in range(1,4):
    G[f'C3{i}'] = {
        'red' : f'C3{i+1}',
        'blue' : False,
        'value' : 29 - i
    }
G['C33']['red'] = 'C0' # center
 
for i in range(1,3):
    G[f'C4{i}'] = {
        'red' : f'C4{i+1}',
        'blue' : False,
        'value' : 25 + i * 5
    }
G['C42']['red'] = 'S20' # center
G['C0'] = {
    'red' : 'C41',
    'blue' : False,
    'value' : 25
}
 
G['G'] = {
    'red' : False,
    'blue' : False,
    'value' : 0
}
 
 
 
ans = 0
def dfs(pieces, res, depth):
    global ans 
    if depth == 10:
        if res > ans:
            ans = res
        return 
    for i in range(4):
        piece, dice = pieces[i], L[depth]
        if piece == 'G':
            continue
        
        piece_next = G[piece]['red'] if not G[piece]['blue'] else G[piece]['blue']
        for _ in range(dice-1):
            if piece_next == 'G':
                break
            piece_next = G[piece_next]['red']
        if piece_next != "G" and piece_next in pieces:
            continue
        res += G[piece_next]['value']
        pieces[i] = piece_next
        dfs(pieces, res, depth+1)
        pieces[i] = piece
        res -= G[piece_next]['value']
    return 
 
dfs(['S0', 'S0', 'S0', 'S0'], 0, 0)
print(ans)