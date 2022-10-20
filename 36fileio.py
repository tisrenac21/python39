# 파일 입출력
# 지금까지 값을 입력받을때는
# 사용자가 직접 키보드로 입력하는 방식을 사용했고
# 값을 출력할때는 모니터 화면에 표시하는 방식을 사용했음

# 하지만, 값을 입력받거나 출력하는 방법은 이게 다가 아님
# 파일을 통해 값을 입력/출력할 수 있고
# 네트워크를 통해 값을 입력/출력할 수도 있음

# 프로그램 실행 중 생성된 데이터(변수)들은
# 주로 메모리 내에 존재하는데 프로그램 종료시 같이 소멸됨(휘발성)
# 데이터의 영속성persistence을 부여하기 위해서는
# 데이터를 저장장치에 보관해서
# 데이터가 소멸되지 않도록 하는 것이 중요!

# 파일쓰기 : 데이터를 파일에 기록
# 파일객체변수 = open(경로, 모드)        # py2
# with open(경로, 모드) as 파일객체변수  # py3

# 파일모드 : 파일작업 종류
# w(쓰기), a(추가쓰기), t(텍스트파일 쓰기),
# b(바이너리파일 쓰기)

# 파일쓰기 작업이 끝나면 반드시 close 해줘야 함
# 단, with문을 사용하는 경우 close 생략 가능

# 간단한 인삿말을 파일에 저장
# open(경로/파일명, 작업모드)
f = open('hello.dat', 'w')      # 쓰기모드로 파일 생성
f.write('Hello, World!!')       # 지정한 파일에 내용 쓰기
f.close()                       # 작업종료 위해 파일 닫음

# with open(경로/파일명, 인코딩, 작업모드) as 별칭    #py3
with open('hello2.dat', 'w', encoding='utf-8') as f:
    f.write('안녕, 디지몬')

# 회원정보를 입력받아 member.dat에 저장
# 저장대상 : 아이디, 비밀번호, 이름, 이메일
# 저장형식 : "아이디/비밀번호/이름/이메일" 형식으로 파일에 저장
# ex) abc123/987xyz/abc123@987xyz.co.kr
userid = input('아이디를 입력하시오: ')
passwd = input('비밀번호를 입력하시오: ')
name = input('이름을 입력하시오: ')
email = input('이메일을 입력하시오')

data = f'{userid}/{passwd}/{name}/{email}'

with open('member.dat', 'a', encoding='UTF-8') as f:
    f.write(data + '\n')

# 학생으로부터 이름,국어,영어,수학 점수를 입력받아
# 파일에 저장하세요 (파일명 : sungjuk.dat)
# 단, 점수는 임의로, 파일에 저장하는 형식은
# "이름,국어,영어,수학" 순으로 작성함
# => 혜교,99,98,99 ( CSV 형식 )
while True:
    if input('성적 입력을 하시겠습니까? Y / N').upper() == 'Y':
        name = input('이름을 입력하시오: ')
        kor = int(input('국어 점수를 입력하시오: '))
        eng = int(input('영어 점수를 입력하시오: '))
        mat = int(input('수학 점수를 입력하시오: '))
        tot = kor + eng + mat
        avg = tot / 3
        grd = '가'
        if avg > 90: grd = '수'
        elif avg > 80: grd = '우'
        elif avg > 70: grd = '미'
        elif avg > 60: grd = '양'

        score = f'{name},{kor},{eng},{mat},{tot},{avg:.1f},{grd}\n'

        with open('sungjuk.dat', 'a', encoding='UTF-8') as f:
            f.write(score)
    else:
        print('프로그램을 종료합니다.')
        break