

'''

괴물 위치는 2번 상하좌우 광선 발사하되 N을 넘지 않는 선에서 끝까지
1 만나면 더이상 뻗어나가기 ㄴㄴ
그러면 괴물 근처 0을 찾아서 변경하고 1을 만나면 break???
하고 나중에 0의 개수 추출하면 되지 않을까 싶긴 한데 흐으으으으으으음
'''


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 외계인 찾기
    for i in range(N):
        for j in range(N):
            if info[i][j] == 2:
                for dir in range(4):
                    # 사방위에 레이저 범위를 1로 시뮬레이션
                    m = 0
                    while True:
                        m += 1
                        if dir == 0:
                            ni = i + di[dir] * m
                            # ni가 유효한 범위인지 먼저 판단
                            if 0 <= ni < N:
                                if info[ni][j] == 1:
                                    break
                                else:
                                    info[ni][j] = 1
                                    continue

                            break
                        if dir == 1:
                            ni = i + di[dir] * m
                            if 0 <= ni < N:
                                if info[ni][j] == 1:
                                    break
                                else:
                                    info[ni][j] = 1
                                    continue
                            break
                        if dir == 2:
                            nj = j + dj[dir] * m
                            if 0 <= nj < N:
                                if info[i][nj] == 1:
                                    break
                                else:
                                    info[i][nj] = 1
                                    continue

                            break
                        if dir == 3:
                            nj = j + dj[dir] * m
                            if 0 <= nj < N:
                                if info[i][nj] == 1:
                                    break
                                else:
                                    info[i][nj] = 1
                                    continue
                            break

    cnt = 0
    # print(N)

    # 시뮬레이션 완료 후 2차원 리스트 완전 탐색
    for i in range(N):
        # print(info[i])
        for j in range(N):
            if info[i][j] == 0:
                cnt += 1

    print(f'#{test_case} {cnt}')


