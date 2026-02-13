T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    idx = N // 2
    jdx = N // 2
    total = 0
    di = 1
    dj = 1
    # print(jdx)

    for i in range((N // 2) + 1):
        total += matrix[i][jdx]
        for j in range(1, di):
            total += matrix[i][jdx - j]
            total += matrix[i][jdx + j]
        di += 1

    for i in range(N - 1, N // 2, -1):
        total += matrix[i][jdx]
        for j in range(1, dj):
            total += matrix[i][jdx - j]
            total += matrix[i][jdx + j]
        dj += 1

    # for i in range(N):
    #     print(matrix[i])

    print(f"#{test_case} {total}")