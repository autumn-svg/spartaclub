def merge(left, right):
    global cnt
    l = r = 0
    result = []

    while len(left) > l and len(right) > r:
        if left[l] > right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    while len(left) > l:
        result.append(left[l])
        l += 1
        if len(left) == l:
            cnt += 1
    while len(right) > r:
        result.append(right[r])
        r += 1

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result = merge_sort(arr)
    print(f"#{test_case} {result[N//2]} {cnt}")