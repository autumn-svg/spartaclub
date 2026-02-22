T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    prev = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for jdx in range(1, j + 1):
            right = i - 1 + jdx
            left = i - 1 - jdx
            if left >= 0 and right < N:
                if prev[right] == prev[left]:
                    if prev[right] == 0:
                        prev[right] = 1
                        prev[left] = 1
                    else:
                        prev[right] = 0
                        prev[left] = 0

    print(f'#{test_case}',end=' ')
    print(*prev)

    # print(f'#{test_case}', *prev)
