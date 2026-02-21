T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    prev = list(map(int, input().split()))

    for _ in range(M): #M개의 줄에 걸쳐 i, j가 주어지기 때문에 for문으로 M만큼 반복
        i, j = map(int,input().split())


        # (1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)
        colour = prev[i-1] # i가 1부터 시작한다는 조건이 나와 있기 때문에 -1을 해 줘야 인덱싱이 맞음
        for k in range(i-1, min(i-1+j, N)): #시작은 i-1이고, j개를 바꾸기 위해 끝은 (i-1 + j)
                                            # 하지만 배열 인덱스는 N-1까지만 가능하므로,
                                            # 끝이 N을 넘지 않도록 min을 사용
            prev[k] = colour # i-1부터 i-1+j-1까지 (총 j개) 색을 변경

    print(f'#{test_case}', *prev) #리스트를 언팩해서 보여줌
