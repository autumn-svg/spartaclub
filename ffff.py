T = int(input())

for tc in range(1, T+1):
    vacant = 0
    sku = 0
    N = list(map(int, input().split()))
    for num in N:
        vacant += num
        sku += 1
    average = vacant/sku
    avg = round(average)
    print(f'#{tc} {avg}')