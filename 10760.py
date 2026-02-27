'''
8방향을 설정하고 현재 위치볻 작은 게 4개 이상일 때 전체 캉ㄴ트 하나 올리기 그리고 그거 출력하기
'''

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
        # print(matrix[_])

    # 정석은 8방위를 설저하는게 먼저
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0 # 4 이상이 된 걸 카운트할 변수

    for i in range(N): #행 우선 순회
        for j in range(M):
            around = 0 # 현재 위치보다 높이가 낮은 걸 세는 변수
            for dx in range(8): # 인덱스로 8방향을 순회하기 위해 for문 설정
                ni = i+di[dx]
                nj = j+dj[dx]
                if 0 <= ni < N and 0 <= nj < M: # 범위를 벗어나면 인덱스 에러가 뜨기 때문에 범위 설정
                    if matrix[ni][nj] < matrix[i][j]:
                        around += 1
            if around >= 4:
                cnt += 1

    print(f"#{test_case} {cnt}")

