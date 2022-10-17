# p78 ex2) 숫자 맞추기 ( 1 ~ 10 )
import random as rnd

magic = rnd.randint(1, 10)  #난수 초기화

while True:
    key = int(input('1 ~ 10의 숫자 중 하나를 입력하세요: '))

    if magic == key:
        print('성공')
        break
    elif magic < key:
        print('숫자가 커요!')
    else:
        print('숫자가 작아요!')


# ex25) 복권 프로그램 - 3자리수 입력 난수 생성 / 사용자 입력
# 난수 범위 - 100 ~ 999, 위치는 상관없이 숫자만 일치여부 판단
# ex) 123 -> 345(1), 317(2), 312(3)
# 문자열 슬라이싱을 위한 문자열 변환 or 함수 사용

# 3개 일치 - 상금 100만원
# 2개 일치 - 상금 5만원
# 1개 일치 - 상금 1천원
# 0개 일치 - 다음 기회에

import random as rnd

lotto = str(rnd.randint(100, 999))
mykey = input('세 자리 복권번호를 입력하세요 (100~999)')
match = 0

# # 첫 째 자리 비교
# if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
#     match += 1
#
# # 둘 째 자리 비교
# if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] == mykey[2]:
#     match += 1
#
# # 셋 째 자리 비교
# if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] == mykey[2]:
#     match += 1

# 개선된 코드 1
for i in range(3):
    if lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[i] == mykey[2]:
        match += 1

# 개선된 코드 1b
for i in range(3):
    if lotto[i] == mykey[0]: match += 1
    if lotto[i] == mykey[1]: match += 1
    if lotto[i] == mykey[2]: match += 1

# 개선된 코드 2
for i in range(3):
    for j in range(3):
        if lotto[i] == mykey[j]:
            match += 1

# 개선된 코드 2b
for i in lotto:
    for j in mykey:
        if i == j:
            match += 1

# 개선된 코드 3
for i in lotto:
    if i in mykey:
        match += 1



# 당첨 여무 판단
if match == 3:
    print('3개 일치 - 상금 100만원')
elif match == 2:
    print('2개 일치 - 상금 30만원')
elif match == 1:
    print('1개 일치 - 상금 1만원')
else:
    print('어떻게 숫자가 한 글자도 안 맞나 ㅋㅋ\n아쉽지만 다음 기회에')


# ex30) 숫자 맞추기 ( 1 ~ 100 )
import random as rnd

num1 = rnd.randint(1, 100)  #난수 초기화

while True:
    num2 = int(input('1 ~ 100의 숫자 중 하나 입력하세요: '))

    if num1 < num2: print('숫자가 커요')
    elif num1 > num2: print('숫자가 작아요')
    else:
        print('빙고!')
        break

