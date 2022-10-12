# 1
# 프로그래밍 언어 실습시 글꼴은 고정폭 글꼴을 사용할 것을 추천.
import datetime
print('=================== 1 ====================')
print('*   *     **     ****     ****     *   *     /////  ')
print('*   *    *  *    *   *    *   *    *   *    | o o | ')
print('*****   *    *   ****     ****      * *    (|  ^  |)')
print('*   *   ******   *   *    *   *      *      | [_] | ')
print('*   *   *    *   *    *   *    *     *       _____  ')
print('')

# 3
print('=================== 3 ====================')
rate1 = 1
# 1stPlayer =2      # 변수명이 숫자로 불가
# myprogram.java    # . 때문에 불가
long = 4
TimeLimit = 5
numberOfWindows = 6

# 4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8

print(3 * x, 3 * x + y, (x + y) / 7)
print(s0 + v0*t + (1/2) * g * t**2)
print('')

# 6
print('=================== 6 ====================')
x, y, m, n = 2.5, 1.5, 18, 4

print(x + n * y - (x + n) * y)
print(m / n  + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 - (1 - n))))

# 가: -1.25
# 나: 6.5
# 다: 11.7
# 라: -3

print('')

# 7
print('=================== 7 ====================')
print(3 + 4.5 * 2 + 27 / 8)
# 논리연산시 경우에 따라 단축식 평가가 적용되기도 함
print(True or False and 3 < 4 or not (5 == 7))
print(True or 3 < 5 and 6 >= 2)
# print(not True > 'A')
print(not True > bool('A'))  # not (True > True)

# print(7 % 4 + 3 - 2 / 6 * 'Z')
print(7 % 4 + 3 - 2 / 6 * bool('Z'))

# print('D' + 1 + 'M' % 2 / 3)
print(bool('D') + 1 + bool('M') % 2 / 3)

print(5.0 / 33. + 2 / 3)
print(53 % 21 < 45 / 18)

print((4 < 6) or True and False or False and (2>3))

print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))
print('')

# 9
print('=================== 9 ====================')
print(True and False and True or True)
print(True or True and True and False)
print((True and False) or (True and (not False)) or (False and (not False)))
print((2 < 3) or (5 > 2) and (not 4 == 4) or 9 != 4)
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)
print('')

# 10
print('=================== 10 ====================')
print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)

# 논리식의 산술식(값)이 결합된 수식에서는
# 논리식의 결과가 True면 값이 출력
# 논리식의 결과가 False면 False가 출력
print((3 < 4) and 5 / 8)

print(23 / 5 + 23 / 5.0)

# print(2.0 + 'a')          # 문자와 정수/실수간 산술연산 불가
# print(2 + 'a')

print('a' + 'b')
# print('a' / 'b')          # 문자간 산술연산 불가
print('a' and not 'b')
print('a' and 'b')

# print((float)'a' / 'b')   # 문자는 실수로의 형변환 불가
print('')

# 11
print('=================== 11 ====================')
name = '홍길동'
weight = 70
age = 35
print('')


# 12
print('=================== 12 ====================')
birthYear = 1996
currentYear = 2022
isPassBirth = True

age = currentYear - birthYear

print('연나이', age)
print('세는나이', age + 1)

# 파이썬의 if 단축키 : 참일때만 if 조선식 else 거짓일 때 값
print('만나이', age if isPassBirth else (age-1))
print('')


# 13
print('=================== 13 ====================')
print('7 X 1 = ', (7*1))
print('7 X 2 = ', (7*2))
print('7 X 3 = ', (7*3))
print('7 X 4 = ', (7*4))
print('7 X 5 = ', (7*5))
print('7 X 6 = ', (7*6))
print('7 X 7 = ', (7*7))
print('7 X 8 = ', (7*8))
print('7 X 9 = ', (7*9))
print('')

# % 서식
print('===== % 서식 =====')
print('7 X 1 = %d'% (7*1))
print('7 X 2 = %d'% (7*2))
print('7 X 3 = %d'% (7*3))
print('7 X 4 = %d'% (7*4))
print('7 X 5 = %d'% (7*5))
print('7 X 6 = %d'% (7*6))
print('7 X 7 = %d'% (7*7))
print('7 X 8 = %d'% (7*8))
print('7 X 9 = %d'% (7*9))
print('')


# .format
print('===== .format 서식 =====')
print('7 X 1 = {0:d}'.format(7*1))
print('7 X 2 = {0:d}'.format(7*2))
print('7 X 3 = {0:d}'.format(7*3))
print('7 X 4 = {0:d}'.format(7*4))
print('7 X 5 = {0:d}'.format(7*5))
print('7 X 6 = {0:d}'.format(7*6))
print('7 X 7 = {0:d}'.format(7*7))
print('7 X 8 = {0:d}'.format(7*8))
print('7 X 9 = {0:d}'.format(7*9))
print('')



# f-string
print('===== f-string 서식 =====')
print(f'7 X 1 = {(7*1):02d}')
print(f'7 X 2 = {(7*2):02d}')
print(f'7 X 3 = {(7*3):02d}')
print(f'7 X 4 = {(7*4):02d}')
print(f'7 X 5 = {(7*5):02d}')
print(f'7 X 6 = {(7*6):02d}')
print(f'7 X 7 = {(7*7):02d}')
print(f'7 X 8 = {(7*8):02d}')
print(f'7 X 9 = {(7*9):02d}')

