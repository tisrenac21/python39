# 20


# 22


# 26 - 연봉/결혼 여부 세금 계산
isMarried = bool(int(input('기혼 "1" / 미혼 "0" 입력')))
salary = int(input('당신의 연봉을 입력하세요(만원단위 생략): '))

if isMarried:
    if salary >= 6000:
        tax = salary * 0.35
    else:
        tax = salary * 0.15
else:
    if salary >= 6000:
        tax = salary * 0.25
    else:
        tax = salary * 0.1

print(f'당신의 세금은 {tax:.0f}만원 입니다.')


# 27 - 윤년 여부
# 2020, 2008, 2000 윤년
# 2022, 1900, 2010 평년
year = int(input("연도를 입력하시오"))
if ((year % 4 == 0 and year % 100 != 0)
        or year % 400 == 0):
    print(f'{year}년은 윤년입니다.')
else:
    print(f'{year}년은 윤년이 아닙니다.')


# 25 - 복권 발행 프로그램
