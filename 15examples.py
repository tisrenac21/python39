# ex48) 복리 계산 - 강사님 버젼
money = 25000       # 통장잔액
inter = 1.06        # 이율
limit = money * 2

# while True:
#     if money > limit:
#         break
#     money = money * inter

for i in range(999):
    if money > limit: break
    money = money * inter

print(f'{i} 년째, 잔액은 {money:,.0f}원')



# # ex48) 복리 계산 - 내가 한 버젼 (입력 받는 버젼)
# amount = int(input('원금을 입력하세요: '))
# inter = int(input('연 이율(%)를 입력하세요: '))
# interest = amount
# year = 0
#
# while interest <= (amount * 2):
#     year += 1
#     interest += interest * (inter / 100)
#
# print(f'원금 {amount:,d}원에 연 이율 {inter}%를 적용하면\n{year}년 뒤에 2배 수익이 납니다.')


# # ex48) 복리 계산 - 내가 한 버젼 (고정값)
# amount = 25000
# interest = amount
# year = 0
#
# while interest <= (amount * 2):
#     year += 1
#     interest += interest * 0.06
#
# print(f'원금 {amount:,d}원에 연 이율 6%를 적용하면\n{year}년 뒤에 2배 수익이 납니다.')






# ex51) 구구단 테이블 출력



# ex53) 입력한 연도의 1월 달력 출력
year = int(input('연도를 입력하시오: '))
exyear31 = ((year-1)*365 + (year-1)/4 - (year-1)/100 + (year-1)/400) % 7

# 0 : 일, 1 : 월, 2 : 화, … … , 6 : 토
# print(int(exyear31)) # 2021년 12월 31일의 요일
print(int(exyear31) + 1) # 2022년 01월 01일의 요일