# ex) 주민번호에서 생년과 월, 일, 성별을 추출해서
# 각 변수에 적절히 저장하세요.
jumin = '202210092123456'

year = int(jumin[:4])
month = int(jumin[4:6])
day = int(jumin[6:8])
if int(jumin[8]) == 2:
    gender = '여'
elif int(jumin[8]) == 1:
    gender = '남'

info = f'''
출생연도 : {year:d}년
출생월일 : {month:02d}월 {day:02d}일
성별 : {gender:s}
'''

print(info)

# 14 - 시간 계산
time = 1234567890
days = time // 86400    # 정수부만 추출

time = 98765
hours = time / 3600

time=12345
mins = time // 60

# 16 - 잔돈 계산
# 비용과 지불금액을 입력받아 잔돈 계산
price = int(input('비용을 입력하세요 : '))
pay = int(input('지불금액 : '))
change = pay - price

print(f'가격은 {price:d}원 이고,\n받은 금액은 {pay:d}원 이고,\n잔액은 {change:d}원 입니다.')

cash50000 = change // 50000
change = change % 50000

cash10000 = change // 10000
change = change % 10000

cash5000 = change // 5000
change = change % 5000

cash1000 = change // 1000
change = change % 1000

cash500 = change // 500
change = change % 500

cash100 = change // 100
change = change % 100

cash50 = change // 50
change = change % 50

cash10 = change // 10
change = change % 10

# 파이썬에서 제공

ment = f'''
50,000원권은 {cash50000:d}장, 10,000원권은 {cash10000:d}장,
5,000원권은 {cash5000:d}장, 1,000원권은 {cash1000:d}장,
500원은 {cash500:d}개, 100원은 {cash100:d}개,
50원은 {cash50:d}개, 10원은 {cash10:d}개입니다.
'''

print(ment)


# 가격은 ???원 이고,
# 받은금액은 ???원 이고,
# 잔액은 ???원 입니다.

# 50,000원권은 ?장, 10,000원권은 ?장,
# 5,000원권은 ?장, 1,000원권은 ?장,
# 500원은 ?개, 100원은 ?개,
# 50원은 ?개, 10원은 ?개입니다.
