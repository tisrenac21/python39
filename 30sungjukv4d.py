# 함수를 이용한 성적처리 프로그램

# 함수 정의부
def displayMenu():
    main_menu = f'''성적 처리 프로그램 v4d
------------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
------------------------'''
    print(main_menu)


def inputSungJuk():
    name = input('이름: ')
    kor = int(input('국어 성적: '))
    eng = int(input('영어 성적: '))
    mat = int(input('수학 성적: '))

    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}

    return sj


def addSungJuk():
    print(' == 학생 및 성적 정보 입력 == ')
    # 성적 데이터 입력 받기
    sj = inputSungJuk()

    # 입력받은 성적데이터 초기화
    tot, avg, grd = compluteSungjuk(sj)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    sjs.append(sj)


def readSungJuk():
    hdr = '이름\t\t총점\t\t등급\n'
    hdr += '----------------------'
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]}        {sj["tot"]}         {sj["grd"]}')


def readOneSungJuk():
    name = input('조회할 학생의 이름은?')
    sj = None
    hdr = '이름\t국어\t영어\t수학\t총점\t평균\t등급\n'
    hdr += '------------------------------------------------------'
    print(hdr)
    for item in sjs:
        if item['name'] == name: sj = item

    for k in sj.keys():
        print(sj.get(k), '\n', end='\t\t')


def modifySungJuk():
    name = input('수정할 학생 이름: ')

    idx = None
    for i in range(len(sjs)):  # 입력한 이름과 일치하는 항복을 sjs에서 찾음
        if (sjs[i])['name'] == name:
            idx = i
            break

    # 새로운(기존) 값을 입력받음
    kor = int(input(f'새로운 국어는? ({sjs[idx]["kor"]})'))
    eng = int(input(f'새로운 영어는? ({sjs[idx]["eng"]})'))
    mat = int(input(f'새로운 수학는? ({sjs[idx]["mat"]})'))

    # 다시 성적 처리
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    tot, avg, grd = compluteSungjuk(sj)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    # 기존 위치에 다시 저장
    sjs[idx] = sj


def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름을 입력하세요: ')

    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인덱스 조사
        item = sjs[i]
        if item['name'] == name:
            idx = i

    sjs.pop(idx)

def compluteSungjuk(sj):
    tot = sj['kor'] + sj['eng'] + sj['mat']
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'

    elif avg >= 80:
        grd = '우'

    elif avg >= 70:
        grd = '미'

    elif avg >= 60:
        grd = '양'

    return tot, avg, grd



# 성적데이터 저장할 변수 선언
sjs = []


# 프로그램 주 실행부
while True:
    # 메뉴 표시 및 값 입력
    displayMenu()
    menu = input('=> 메뉴를 선택해주세요: ')

    if menu == '1': addSungJuk()
    elif menu == '2': readSungJuk()
    elif menu == '3': readOneSungJuk()
    elif menu == '4': modifySungJuk()
    elif menu == '5': removeSungJuk()
    elif menu == '0': break
    else: print('잘못된 입력입니다.')
    