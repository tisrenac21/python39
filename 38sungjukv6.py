# 파일입출력을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 함수들은 sungjukv6lib.py에 작성함
# 모듈명은 sjv5로 줄여서 사용함

# 성적데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부
import sungjukv6lib as sjv6

# 파일에 저장된 성적데이터 불러오기
sjv6.loadSungJuk()
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv6.displayMenu()

    if menu == '1':
        sjv6.addSungJuk()
    elif menu == '2':
        sjv6.readSungJuk()
    elif menu == '3':
        sjv6.readOneSungJuk()
    elif menu == '4':
        sjv6.modifySungJuk()
    elif menu == '5':
        sjv6.removeSungJuk()
    elif menu == '0':
        # 메모리에 존재하는 성적데이터를 파일에 저장
        # sjv6.saveSungJuk()
        break
    else:
        print('잘못된 입력입니다.')