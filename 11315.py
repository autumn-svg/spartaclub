
'''
가로, 세ㅔ로, 대각선을 설정 해 놓고 쭉 갔을 때 o가 있으면 카운트+1
카운트가 5개가 되면 yes 출력
'''

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]

    result = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for idx in range(4):
                    for m in range(5):
                        ni = i + di[idx] * m
                        nj = j + dj[idx] * m
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] != 'o':
                                break
                            if m == 4 and arr[ni][nj] == 'o':
                                result = 'YES'

    print(f'#{test_case} {result}')
