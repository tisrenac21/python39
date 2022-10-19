# 2차원 리스트와 dict를 이용한 성적 처리 프로그램

# 성적데이터 저장할 변수 선언
sjs = []

# 프로그램 메뉴 출력을 위한 변수 선언
main_menu = f'''
성적 처리 프로그램 v3
------------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
------------------------
'''

# 프로그램 주 실행부
while True:
    print(main_menu)
    menu = input('=> 메뉴를 선택하세요 : ')

    if menu == '0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  # 성적데이터 입력, 성적처리
        print(' == 학생 및 성적 정보 입력 == ')
        name = input('이름: ')
        kor = int(input('국어 성적: '))
        eng = int(input('영어 성적: '))
        mat = int(input('수학 성적: '))

        tot = kor + eng + mat
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

        sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

        sjs.append(sj)

        input('성적 데이터 추가 완료!')

    elif menu == '2':  # 이름, 국어, 영어, 수학만 출력
        hdr = '이름\t\t총점\t\t등급\n'
        hdr += '----------------------'
        print(hdr)

        for sj in sjs:
            print(f'{sj["name"]}        {sj["tot"]}         {sj["grd"]}')

        input('성적 데이터 조회 완료!')

    elif menu == '3':
        name = input('조회할 학생의 이름은?')
        sj = None
        hdr = '이름\t국어\t영어\t수학\t총점\t평균\t등급\n'
        hdr += '------------------------------------------------------'
        print(hdr)
        for item in sjs:
            if item['name'] == name: sj = item

        for k in sj.keys():
            print(sj.get(k), end='\t\t')




        # search = input('검색할 학생의 이름을 입력하세요.')
        # cnt = 0
        # hdr = '번호\t\t이름\t\t총점\t\t등급\n'
        # hdr += '----------------------'
        # print(hdr)
        # for i in range(len(names)):
        #     if names[i] == search:
        #         cnt += 1
        #         print(f'{cnt}번:  {names[i]}     {tots[i]}       {grds[i]}')
        #
        # prompt = int(input('상세 조회를 원하는 학생의 번호를 숫자만 입력하세요: '))
        # cnt = 0
        # hdr = '이름\t국어\t영어\t수학\t총점\t평균\t등급\n'
        # hdr += '------------------------------------------------------'
        # print(hdr)
        # for i in range(len(names)):
        #     if names[i] == search:
        #         cnt += 1
        #         if cnt == prompt:
        #             print(f'{names[i]}     {kors[i]}       {engs[i]}       {mats[i]}        {tots[i]}       '
        #                   f'{avgs[i]}       {grds[i]}')

        input('\n성적 데이터 상세조회 완료!')

    elif menu == '4':
        name = input('수정할 학생 이름: ')

        idx = None
        for i in range(len(sjs)):    # 입력한 이름과 일치하는 항복을 sjs에서 찾음
            if (sjs[i])['name'] == name:
                idx = i
                break

        # 새로운(기존) 값을 입력받음
        kor = int(input(f'새로운 국어는? ({sjs[idx]["kor"]})'))
        eng = int(input(f'새로운 영어는? ({sjs[idx]["eng"]})'))
        mat = int(input(f'새로운 수학는? ({sjs[idx]["mat"]})'))
        
        # 다시 성적 처리
        tot = kor + eng + mat
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

        # 값 다시 저장
        sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}
        
        # 기존 위치에 다시 저장
        sjs[idx] = sj

        input('성적 데이터 수정 완료!')

    elif menu == '5':
        name = input('삭제할 데이터의 학생 이름을 입력하세요: ')

        idx = None
        for i in range(len(sjs)):       # 삭제할 데이터의 인덱스 조사
            item = sjs[i]
            if item['name'] == name:
                idx = i

        sjs.pop(idx)


        input('\t성적 데이터 삭제 완료!')

    else:
        print('잘못된 번호를 입력했습니다.')
