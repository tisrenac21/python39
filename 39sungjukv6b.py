# json 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 함수들은 sungjukv6lib.py에 작성함
# 모듈명은 sjv5로 줄여서 사용함

# 성적데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부

# 파일에 저장된 성적데이터 불러오기
# 프로그램 시작전 데이터 초기화
import sungjukv6blib as sjv6b

# 파일에 저장된 성적데이터 불러오기
sjv6b.loadSungJuk()
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv6b.displayMenu()

    if menu == '1':
        sjv6b.addSungJuk()
    elif menu == '2':
        sjv6b.readSungJuk()
    elif menu == '3':
        sjv6b.readOneSungJuk()
    elif menu == '4':
        sjv6b.modifySungJuk()
    elif menu == '5':
        sjv6b.removeSungJuk()
    elif menu == '0':
        break
    else:
        print('잘못된 입력입니다.')