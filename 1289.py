T = int(input())
for test_case in range(1,T+1):
    stc = input() #비교할 값을 문자열로 보고 비교할 거기 때문에 걍 인풋으로 받음

    previous = '0' #비교할 문자열
    cnt = 0 #횟수 셀 거
    for i in stc: #문자열 하나하나 해체
        if i != previous: #비교할 문자열과 비교해서 같지 않으면
            previous = i #그걸 i와 같게 바꾸고
            cnt += 1 #횟수 하나 추가

    print(f'#{test_case} {cnt}')
