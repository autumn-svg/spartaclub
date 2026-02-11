T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    vacant = 0
    for num in lst:
        if num % 2 == 1:
            vacant += num

    print(f'#{tc} {vacant}')
