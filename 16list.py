# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리


# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 3명의 학생에 대해 성적처리를 진행함
# 변수 초기화

# 1 - 1
# name1 = '혜교'
# name2 = '지현'
# name3 = '수지'

# 1 - 2
name1, name2, name3 = '혜교', '지현', '수지'
kor1, kor2, kor3 = 99, 75, 65
# ...
# 처리할 데이터 갯수에 따라 변수를 일일이 선언해야 함 ㅡ 불편!

# tot1 = kor1 + eng1 + mat1
# tot2 = kor2 + eng2 + mat2
# tot3 = kor3 + eng3 + mat3
# ...
# 성적 처리 시에도 동일한 코드를 여러번 반복해 작성함 ㅡ 번거로움!
# => 이러한 문제를 해결하기 위해 자료구조와 관련된 기술을 사용

# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복 허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근(참조)하려면 변수[인덱스] 형식을 사용

# 점심 메뉴를 리스트로 정의
menus = ['라면', '돈가스', '짜장면', '냉면', '정식']
print(menus)

# 리스트에서 일부 요소 item만 출력
print(menus[0], menus[2], menus[4])
print(f'{menus[0]}, {menus[2]}, {menus[4]}')

# 리스트의 모든 요소 출력
print(menus[0], menus[1], menus[2], menus[3], menus[4])

# 위와 같이 출력하면 번거로우니 반복문으로 출력
for i in range(len(menus)):
    print(menus[i], end=' ')

print()

# 리스트의 모든 요소를 반복문으로 출력 2
# for 변수 in 객체
for menu in menus:  # 리스트의 요소를 하나씩 훑어가며 출력
    print(menu, end=' ')

# 동적으로 리스트 생성하기
menuses = []      # 빈 리스트 선언

# 리스트에 요소를 추가하려면 append 함수
# append 한 요소는 리스트의 맨 뒤에 부착 ㅡ FIFO
menuses.append('라면')
menuses.append('돈가스')
menuses.append('자장면')
menuses.append('우동')
menuses.append('정식')


# 지정한 위치에 새로운 요소 추가 : insert(인덱스, 값)
# 지정한 인덱스에 이미 값이 존재하면 그 값부터 하나씩 뒤로 밀림
menuses.insert(3, '냉면')   #이렇게 넣으면 우동이 4번, 정식이 5번으로 밀린다

# 리스트 요소의 값 수정 : 객체명[인덱스] = 새로운 값
print(menuses[3])
menuses[3] = '탕수육'
print(menuses[3])

# 리스트 요소 삭제 : 값으로 삭제하는 방법( remove(값) ), 위치로 삭제하는 방법( pop(인덱스) )
menuses.remove('탕수육')
menuses.pop(2)

# pop() ㅡ 뒤에서부터 차례대로 삭제
menuses.pop()

# 리스트로 다양한 데이터 다루기
datas = []

datas.append(1)
datas.append(2.5)
datas.append(True)
datas.append('Hello')
datas.append([1, 3, 5])

print(datas)

print(menuses + datas)





# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 리스트를 이용해서 3명의 학생에 대해 성적처리를 진행함


# 변수선언 및 초기화
names = ['혜교', '지현', '수지']
kors = [85, 95, 100]
engs = [80, 75, 85]
mats = [95, 90, 100]
avgs = [0, 0, 0]
tots = [0, 0, 0]
grds = ['가', '가', '가']

# 성적 처리 1
tots[0] = kors[0] + engs[0] + mats[0]
tots[1] = kors[1] + engs[1] + mats[1]
tots[2] = kors[2] + engs[2] + mats[2]

avgs[0] = tots[0]/3
avgs[1] = tots[1]/3
avgs[2] = tots[2]/3

if avgs[0] >= 90: grds[0] = '수'
elif avgs[0] >= 80: grds[0] = '우'
elif avgs[0] >= 70: grds[0] = '미'
elif avgs[0] >= 60: grds[0] = '양'

if avgs[1] >= 90: grds[1] = '수'
elif avgs[1] >= 80: grds[1] = '우'
elif avgs[1] >= 70: grds[1] = '미'
elif avgs[1] >= 60: grds[1] = '양'

if avgs[2] >= 90: grds[2] = '수'
elif avgs[2] >= 80: grds[2] = '우'
elif avgs[2] >= 70: grds[2] = '미'
elif avgs[2] >= 60: grds[2] = '양'

#결과출력 1
print(names[0], kors[0], engs[0], mats[0],tots[0], avgs[0], grds[0])
print(names[1], kors[1], engs[1], mats[1],tots[1], avgs[1], grds[1])
print(names[2], kors[2], engs[2], mats[2],tots[2], avgs[2], grds[2])


# 성적처리 2
for i in range(len(names)):
    tots[i] = kors[i] + engs[i] + mats[i]
    avgs[i] = tots[i]/3
    if avgs[i] >= 90: grds[i] = '수'
    elif avgs[i] >= 80: grds[i] = '우'
    elif avgs[i] >= 70: grds[i] = '미'
    elif avgs[i] >= 60: grds[i] = '양'

# 결과출력 2
for i in range(len(names)):
    print(names[i], kors[i], engs[i], mats[i],tots[i], avgs[i], grds[i])


# p110 ex1)
lst = [10, 1, 5, 2]     # list 생성

result = lst * 2
print(result)

result.append(result[0] * 2)
print(result)

result2 = []
result2 = result[1::2]
print(result2)


# p110 ex2 - A) -- 강사님 버젼
import random as rnd
lst = []
size = int(input('vector 수: '))

for i in range(size):
    val = rnd.randint(1, 10)
    print(val)
    lst.append(val)

print(f'리스트의 크기 : {len(lst)}')


# p110 ex2 - B
import random as rnd
lst = []
size = int(input('vector 수: '))

for i in range(size):
    val = rnd.randint(1, 10)
    print(val)
    lst.append(val)

key = int(input('리스트에서 찾을 값: '))

# 검색기능 1
isFind = 'NO'
for i in range(size):
    if lst[i] == key:
        isFind = 'YES'
print(isFind)

# 검색기능 2
isFind = 'NO'
for val in lst:
    if val == key:
        isFind = 'YES'
print(isFind)

# 검색기능 3 ㅡ if 값 in 객체 - 객체에서 특정값 존재 여부 확인
isFind = 'NO'
if key in lst: isFind = 'YES'
print(isFind)




# p110 ex2 - A) -- 내가 한 버젼
# import random as rnd
#
# vector = int(input('vector 수: '))
# rannum = []
# for i in range(vector):
#     rannum.append(rnd.randint(0, 9))
#     print(rannum[i])
#
# print(f'vector 크기: {len(rannum)}')


# employees.csv를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid

empnos = []
fnames = []
lnames = []
emails = []
hdates = []
jobids = []
sals = []
deptids = []

empno = input('사원번호를 입력하시오: ')
fname = input('이름을 입력하시오: ')
lname = input('성을 입력하시오: ')
email = input('이메일을 입력하시오: ')
hdate = input('입사일을 입력하시오: ')
jobid = input('직책을 입력하시오: ')
sal = input('급여를 입력하시오: ')
deptid = input('부서번호를 입력하시오: ')

empnos.append(empno)
fnames.append(fname)
lnames.append(lname)
emails.append(email)
hdates.append(hdate)
jobids.append(jobid)
sals.append(sal)
deptids.append(deptid)

# 저장된 모든 사원정보를 출력
for i in range(len(empnos)):
    print(f'사원번호: {empnos[i]}, 이름: {lnames[i]}{fnames[i]}, 이메일: {emails[i]}, 입사일: {hdates[i]}, 직책: '
          f'{jobids[i]}, 급여: {sals[i]}, 부서번호: {deptids[i]}')

# 다루어야 하는 데이터의 항목수가 많을 수록
# 일일이 리스트로 선언해서 저장하는 것은 다소 불편
# => 딕서너리, 클래스를 이용하면 편리하게 다룰 수 있음


