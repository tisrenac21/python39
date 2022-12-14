# 마리아디비를 이용한 성적처리 프로그램
# 성적 처리 프로그램의 함수들은 sungjukv7lib.py에 작성함
# 모듈명은 sjv7로 줄여서 사용함

# 성적데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부

# 파일에 저장된 성적데이터 불러오기
# 프로그램 시작전 데이터 초기화
import sungjukv7lib as sjv7c

# 파일에 저장된 성적데이터 불러오기
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv7c.displayMenu()

    if menu == '1':
        sjv7c.addSungJuk()
    elif menu == '2':
        sjv7c.readSungJuk()
    elif menu == '3':
        sjv7c.readOneSungJuk()
    elif menu == '4':
        sjv7c.modifySungJuk()
    elif menu == '5':
        sjv7c.removeSungJuk()
    elif menu == '0':
        break
    else:
        print('잘못된 입력입니다.')