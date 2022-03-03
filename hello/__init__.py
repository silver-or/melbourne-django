from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz06RandomGenerator, \
    Quiz07RandomChoice, Quiz08Rps, Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, \
    Quiz14Gugudan

if __name__ == '__main__':
    while 1:
        menu = int(input('\n0. Exit\n'
                         '1. calculator\n'
                         '2. bmi\n'
                         '3. grade\n'
                         '4. gradeAuto\n'
                         '5. dice\n'
                         '6. randomGenerator\n'
                         '7. randomChoice\n'
                         '8. rps\n'
                         '9. getPrime\n'
                         '10. leapYear\n'
                         '11. numberGolf\n'
                         '12. lotto\n'
                         '13. bank\n'
                         '14. gugudan\n'))
        s = '*' * 30 + '\n'
        if menu == 0:
            break
        elif menu == 1:
            q1 = Quiz01Calculator(int(input('첫 번째 숫자 : ')), input('연산자 (+, -, *, /) : '), int(input('두 번째 숫자 : ')))
            s += q1.calculate()
        elif menu == 2:
            m = Member()
            m.name = input('이름 : ')
            m.height = float(input('키 : '))
            m.weight = float(input('몸무게 : '))
            res = Quiz02Bmi.getBmi(m)
            s += f'{m.name}님의 비만도 결과는 {res}입니다.'
        elif menu == 3:
            q3 = Quiz03Grade(input('이름 : '), int(input('국어 점수 : ')), int(input('영어 점수 : ')), int(input('수학 점수 : ')))
            s += f'[성적표]\n이름 : {q3.name}\n국어 점수 : {q3.kor}\n영어 점수 : {q3.eng}\n수학 점수 : {q3.math}\n평균 : {q3.avg:.2f}\n합격 여부 : {q3.checkPass()}\n학점 : {q3.getGrade()}'
        elif menu == 4:
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                print(i)
        elif menu == 5:
            s += f'주사위 숫자 : {Quiz05Dice.cast()}'
        elif menu == 6:
            q6 = Quiz06RandomGenerator(int(input('시작값 : ')), int(input('끝값 : ')))
            s += f'생성된 난수 : {q6.execute()}'
        elif menu == 7:
            s += f'추출 결과 : {Quiz07RandomChoice().execute()}'
        elif menu == 8:
            q8 = Quiz08Rps(int(input('1~3 사이의 수 입력 : (1 : 가위, 2 : 바위, 3 : 보) ')))
            s += q8.execute()
        elif menu == 9:
            q9 = Quiz09GetPrime(int(input('시작값 : ')), int(input('끝값 : ')))
            s += f'입력 범위 내 소수 : {q9.execute()}'
        elif menu == 10:
            s += Quiz10LeapYear(int(input('연도 입력 : '))).execute()
        elif menu == 11:
            s += Quiz11NumberGolf().execute()
        elif menu == 12:
            s += Quiz12Lotto().execute()
        elif menu == 13:
            s += Quiz13Bank().execute()
        elif menu == 14:
            s += Quiz14Gugudan.execute()
        else:
            s += '0~14 사이의 수를 입력해주세요.'
        print(s)
