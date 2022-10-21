# 마리아디비를 이용한 성적처리 프로그램
# 성적 처리 프로그램의 함수들은 sungjukv7lib.py에 작성함
# 모듈명은 sjv7로 줄여서 사용함

# 성적데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부

# 파일에 저장된 성적데이터 불러오기
# 프로그램 시작전 데이터 초기화
import sungjukv6clib as sjv6c

# 파일에 저장된 성적데이터 불러오기
sjv6c.loadSungJuk()
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv6c.displayMenu()

    if menu == '1':
        sjv6c.addSungJuk()
    elif menu == '2':
        sjv6c.readSungJuk()
    elif menu == '3':
        sjv6c.readOneSungJuk()
    elif menu == '4':
        sjv6c.modifySungJuk()
    elif menu == '5':
        sjv6c.removeSungJuk()
    elif menu == '0':
        break
    else:
        print('잘못된 입력입니다.')