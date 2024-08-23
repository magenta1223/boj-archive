#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9202                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9202                          #+#        #+#      #+#     #
#     Solved: 2024-08-23 06:08:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline

def _find(boggle, i,j, word):
    end = len(word)
    def dfs(x,y,idx):
        if idx == end:
            return True 
        res = False 
        for dx, dy in D:
            nx,ny = x+dx, y+dy 
            if 0<=nx<4 and 0<=ny<4 and not visited[nx][ny] and boggle[nx][ny] == word[idx]:
                visited[nx][ny] = True 
                res = any([res, dfs(nx,ny,idx+1)])
                visited[nx][ny] = False 
        return res 
    
    visited = [ [False] * 4 for _ in range(4)]
    visited[i][j] = True
    return dfs(i,j,1) if boggle[i][j] == word[0] else False 


def find(boggle, word):    
    done = False

    for i in range(4):
        for j in range(4):
            done = _find(boggle, i,j,word)
            if done:
                break 
        if done:
            break 
    return done 

SCORES = [0,0,0,1,1,2,3,5,11]
D = [(-1,0),(-1,1),(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

W = int(input())
WORDS = [input().strip() for _ in range(W)]
input()

B = int(input())
Boggles = []

for _ in range(B):
    Boggles.append([list(input().strip()) for _ in range(4)])
    input()



for boggle in Boggles:
    score, longest_word, maxlen, cnt = 0, "", 0, 0    
    for w in WORDS:
        if find(boggle, w):
            score += SCORES[len(w)]
            cnt += 1 
            if len(w) > maxlen:
                maxlen = len(w)
                longest_word = w 
            elif len(w) == maxlen: #시바 
                longest_word = sorted([longest_word, w])[0]
    if longest_word:
        print(score, longest_word, cnt)
    else:
        print("0 0")
    
