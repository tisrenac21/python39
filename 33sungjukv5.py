# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 함수들은
# sungjukv5lib.py에 작성함
# 모듈명은 sjv5로 줄여서 사용함

# 성적데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부
import mldl.sungjukv5lib as sjv5

while True:
    # 메뉴 표시 및 값 입력
    menu = sjv5.displayMenu()

    if menu == '1':
        sjv5.addSungJuk(sjs)
    elif menu == '2':
        sjv5.readSungJuk(sjs)
    elif menu == '3':
        sjv5.readOneSungJuk(sjs)
    elif menu == '4':
        sjv5.modifySungJuk(sjs)
    elif menu == '5':
        sjv5.removeSungJuk(sjs)
    elif menu == '0':
        break
    else:
        print('잘못된 입력입니다.')