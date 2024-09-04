# 문명으로 꽉 채워진 경우
# 인접 쌍 개수가 ㅈㄴ많아서> 

N = int(input())
D = f'{N} {N**2}'

for i in range(N):
    for j in range(N):
        D += f'\n{i+1} {j+1}'

with open("./test.txt", mode = "w+") as f:
    f.write(D)

 