# while 반복문
# 횟수와는 상관없이 조건에 따라 반복실행하는 반복문
# 즉, 조건식의 결과가 참이면 실행하고, 거짓일 경우 실행을 중단함

# 변수초기화
# while 조건식:
#    반복실행할 문장
#    증감식

# ex) 1 ~ 100 사이 정수 출력
i = 1
while i <= 100:
    print(i, end=' ')
    i += 1

#1 ex) 1 ~ 100 사이 정수 중 홀수만 출력
i = 1
result = ''
while i <= 100:
    if i % 2 != 0:
        result += str(i) + ' '
    i += 1

print(result)

# ex) 1 ~ 100 사이의 정수들의 모든 합 계산 후 출력
i = 1
hap = 0
while i <= 100:
    hap += i
    i += 1

print(hap)


# ex) 단을 입력받아 해당 단의 구구단을 출력
dan = int(input('구구단 정수를 입력하세요: '))
i = 1
while i <= 9:
    print(f'{dan} X {i} = {dan * i}')
    i += 1


# p79 ex3) 3의 배수지만 2의 배수는 아닌 정수 출력하고 누적합도 계산해서 출력
hap = 0
result = ''
i = 1
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        result += str(i) + ' '
        hap += i
    i += 1
print(result)
print(f'합: {hap}')


# 무한루프
# 반복문의 조건식이 언제나 참이면
# 반복을 중단하지 않고 계속 반복을 지속하는 상황
# 단, 무한루프에서 탈출하려면 break를 이용
# while True:
#    반복실행할 문장

# 반복 실행 중지 : break
# 반복 실행을 중지하고 반복문에서 나올때 사용

# ex) 1~100 사이 정수들의 모든 합 계산후 출력
# 단, 무한루프와 break를 이용해서 작성
i = 1
hap = 0
while True:
    if i <= 100: hap += i
    else: break
    i += 1

print(hap)


# ex) 1 ~ 1000 사이의 모든 정수의 합을 출력하세요
# 단, 누적합이 15000을 넘으면 반복문을 중지하고 결과를 출력
i = 1
hap = 0
while True:
    if hap > 15000: break
    elif i <= 1000: hap += i
    i += 1


# while i <- 1000:
#     if hap > 15000: break
#     hap += i
#     i += 1


print(hap)


main_menu = f'''
성적 처리 프로그램 v1
------------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
------------------------
'''
print(main_menu)
input('=> 작업을 선택하세요 : ')