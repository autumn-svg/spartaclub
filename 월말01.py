T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    the_man = 0
    man = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                the_man += 1
                man.append([i, j])

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for attack in range(the_man):
        i = man[attack][0]
        j = man[attack][1]

        for idx in range(4):
            m = 0
            while True:
                m += 1
                ni = i + (di[idx] * m)
                nj = j + (dj[idx] * m)

                if 0 <= ni < N and 0 <= nj < N:
                    if matrix[ni][nj] == 1:
                        break

                    if matrix[ni][nj] == 0:
                        matrix[ni][nj] = 3

                    continue

                break

    cnt = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                cnt += 1

    print(f"#{test_case} {cnt}")
