# 성적 데이터 저장할 변수 선언
sjs = []

#w sungjuk.dat 파일을 읽어서 sjs 변수에 초기화.
def loadSungJuk():
    global sjs
    # 파일에 저장된 성적데이터들을 행단 위로 읽어 리스트에 저장
    with open('data/sungjuk.dat', encoding='UTF-8') as f:
        data = f.readlines()
    print(data)

    outs = []   # 성적 데이터를 저장하기 위해 리스트 선언
    for d in data:      # 리스트에 저장된 성적데이터에서 한 건씩 읽어와서
        items = d.strip().split(',')    # 읽어온 데이터를 콤마(,)로 분리하고
        item = {'name': items[0], 'kor': items[1], 'eng': items[2], 'mat': items[3],
                'tot': items[4], 'avg': items[5], 'grd': items[6]}
        # 분리한 데이터를 dict 형식으로 재작성 후 dict 으로 작성된 데이터를 리스트에 저장
        outs.append(item)
    sjs = outs

# 성적데이터들을 sungjuk.dat 파일에 저장
# [ {'name': 혜교, 'kor': 77, 'eng': 33, 'mat': 86},
#   {'name': 지현, 'kor': 66, 'eng': 44, 'mat': 54},
#   {'name': 수지, 'kor': 55, 'eng': 55, 'mat': 43} ]
def saveSungJuk(sjs):
    with open('data/sungjuk.dat','w',encoding='UTF-8') as f:
        for sj in sjs:      # 방금 입력한 성적데이터와 기존 입력한 모든 성적데이터를 파일에 함께 저장
            dat = f'{sj["name"]},{sj["kor"]},{sj["eng"]},{sj["mat"]},{sj["tot"]},{sj["avg"]},{sj["grd"]}\n'
            f.write(dat)

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

    # sjs에 저장된 성적데이터를 파일에 저장
    saveSungJuk(sjs)


def displayMenu():
    main_menu = f'''성적 처리 프로그램 v6
------------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
------------------------'''
    print(main_menu)

    return input('=> 메뉴를 선택해주세요: ')


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

    #수정된 성적데이터를 파일에 저장.
    saveSungJuk(sjs)


def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름을 입력하세요: ')

    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인덱스 조사
        item = sjs[i]
        if item['name'] == name:
            idx = i

    sjs.pop(idx)
    
    #삭제된 성적데이터를 파일에 저장.
    saveSungJuk(sjs)
