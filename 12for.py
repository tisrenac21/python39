# 반복문
# 정해짓 횟수 만큼 특정 코드를 실행하도록 만든 문장
# 파이썬에서는 for문과 while 문이 지원

# 만일, 'Hello, world!!!'를 한 번 출력한다면?
# -> print 함수 한 번 사영
print('Hello, world!!!')

# 그런데, 'Hello, World!!!'를 세 번 출력한다면?
print('Hello, world!!!')    # 세 번 출력
print('Hello, world!!!')
print('Hello, world!!!')

# 만일, 100번 출력해야 한다면 복붙을 계속할 것인가?
# 또한, 반복시 출력하는 문구가 변경된다면? - 다시 수정
# 효율적인 반복실행을 위해서 반복문을 사용함

# for 반복변수 in range(시작값, 종료값+1, 증감값);
#     반복실행할 문장

# range 함수 사용하기
# range(숫자) - 0부터 숫자 -1까지의 범위
list(range(10))     # 0 ~ (10 - 1) 범위

# range(시작, 끝+1) - 시작값부터 끝값까지의 범위
list(range(1, 46))

# range(시작, 끝+1, 증감값)
# => 시작값부터 증감값을 처리해서 끝값의 범위까지 출력
list(range(1, 10, 2))
list(range(0, 10, 2))

# ex) 1 ~ 100 사이 정수 출력
# 반복문을 쓰지 않는다면
# print(1)
# print(2)
# print(3)
# ...
# print(99)
# print(100)

# 반복문을 사용한다면
list(range(1, 100, 1))

for i in range(1, 100+1):
    print(i, end=',')
# print 함수러 깂을 출력 시 줄바꿈 문자가 자동 추가 된다.
# 줄바꿈 문자 대신 다른 문자로 대체하려면 end 속성을 사용한다.

# ex) 100 ~ 1 사이 정수 출력
list(range(100, 1, -1))

for i in range(100, 0, -1):
    print(i, end=' ')

# ex) 1 ~ 100 사이 정수 중 짝수만 출력
list(range(2, 100+1, 2))

for i in range(2, 100+1, 2):
    print(i, end=' ')

list(range(1, 100+1))

for i in range(1, 100+1):
    if i % 2 == 0: print(i, end=' ')


# ex) 1 ~ 100 사이 정수들의 모든 합 계산 후 출력
hap = 0
for i in range(1, 100+1):
    hap += i
print(hap)


# 가우스 덧셈 공식을 이용해서
# 1 ~ 100 사이 모든 정수들의 합 계산 후 출력
# x ~ y 까지의 숫자를 더한 합을 구하는 공식
((x + y) * (y - x + 1)) / 2

((1 + 100) * (100 - 1 + 1) / 2)


# 문자열에 반복문 적용하기
# => 문자열에서 문자를 하나씩 가져와서 출력함
for i in 'Hello World':
    print(i, end='')


# ex) 단을 입력받아 해당 단의 구구단을 출력
dan = int(input('구구단 정수를 입력하세요: '))
for i in range(1, 10):
    print(f'{dan} X {i} = {dan * i}')


# p79 ex3) 3의 배수지만 2의 배수는 아닌 정수와 누적합 출력.
hap = 0
result = ''
for i in range(1, 101):
    if i % 3 == 0 and i % 2 != 0:
        result += str(i) + ' '
        hap += i
print(result)
print(f'합: {hap}')
