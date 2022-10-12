# 조건문
# 조건에 따라 프로그램의 실행 순서를 조정하는 문장
# '만약에 ~ 한다면 ~ 하고 아니면 ~ 하라' 라는
# 문제 해결시 주로 사용
# 조건문 내부의 실행문은 반드시 들여쓰기를 사용해야 함!

# if 조건식:
#    참일때 실행할 문장
# else:
#    거짓일때 실행할 문장

# ex1) 입력한 어떤 수가 짝수인지 판단하는 조건문
num = int(input('정수 하나를 입력하세요.'))

if num % 2 == 0:
    print('입력한 수는 짝수입니다.')

# ex2) 점수 3개를 입력받아 평균이 60점 이상이고,
# 각 점수가 40점 이상이면 합격이라 출력하는 조건문 작성
# 50, 60, 65
# 30, 95, 65

jumsu1 = int(input('점수1은? '))
jumsu2 = int(input('점수2은? '))
jumsu3 = int(input('점수3은? '))

if ((jumsu1+jumsu2+jumsu3 / 3) >= 60) and \
        (jumsu1 >= 40 and jumsu2 >= 40 and jumsu3 >= 40):
    print('합격')
else:
    print('불합격')

avg = (jumsu1 + jumsu2 + jumsu3) / 3
is60 = avg >= 60
is40 = (jumsu1 >= 40) and (jumsu2 >= 40) and (jumsu3 >= 40)

if is60 and is40:
    print('합격')
else:
    print('불합격')


# ex3) 입력한 어떤 수가 짝수 / 홀수인지 판단하는 조건문
num = int(input('정수 하나를 입력하세요.'))

if num % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

# ex4) 아이디, 비밀번호를 입력받아
# 미리 설정해준 아이디, 비밀번호와 일치하면 '로그인 성공',
# 일치하지 않으면 '로그인 실패'라고 출력하는 조건문 작성
# 아이디: abc123, 비밀번호: 987xyz
uid = 'abc123'
pwd = '987xyz'

inputid = input('아이디를 입력하세요: ')
inputpwd = input('비밀번호를 입력하세요: ')

lok1 = inputid == uid
lok2 = inputpwd == pwd

if lok1 and lok2:
    print('로그인 성공!')
else:
    print('로그인 실패!')