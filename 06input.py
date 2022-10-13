# input 함수
# 변수명 = input(입력메시지)
# input 함수로 입력받은 내용은 기본적으로 문자로 취급

# 성적처리 프로그램 v2
# 이름과 국어, 영어, 수학의 점수를 입력받아 총점, 평균을 출력함.
name = input('이름을 입력하시오 : ')
kor = int(input('국어 점수를 입력하시오 : '))
eng = int(input('영어 점수를 입력하시오 : '))
mat = int(input('수학 점수를 입력하시오 : '))
tot = kor + eng + mat
avg = tot / 3

print(f'이름 : {name:s}')
print(f'국어: {kor:d}, 영어: {eng:d}, 수학: {mat:d}')
print(f'총점: {tot:d}, 평균 {avg:.2f}')

fat = float(input('지방의 그램을 입력하세요 : '))
carbohydrate = float(input('탄수화물의 그램을 입력하세요 : '))
protein = float(input('단백질의 그램을 입력하세요 : '))
kcal = (fat*9)+(protein*4)+(carbohydrate*4)
print(f'총칼로리 : {kcal:,.2f} cal')

# 성적관리 프로그램의 메뉴화면 작성 1
print('성적 처리 프로그램 v1')
print('------------------------')
print('1. 성적 데이터 추가')
print('2. 성적 데이터 조회')
print('3. 성적 데이터 상세조회')
print('4. 성적 데이터 수정')
print('5. 성적 데이터 삭제')
print('0. 프로그램 종료')
print('------------------------')
print('')

# 성적관리 프로그램의 메뉴화면 작성 2
main_menu = '성적 처리 프로그램 v1 \n'
main_menu += '------------------------\n'
main_menu += '1. 성적 데이터 추가\n'
main_menu += '2. 성적 데이터 조회\n'
main_menu += '3. 성적 데이터 상세조회\n'
main_menu += '4. 성적 데이터 수정\n'
main_menu += '5. 성적 데이터 삭제\n'
main_menu += '0. 프로그램 종료\n'
main_menu += '------------------------'
print(main_menu)

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