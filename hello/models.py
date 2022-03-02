import random

def main():
    while 1:
        menu = int(input('\n0. Exit\n'
                         '1. 계산기\n'
                         '2. BMI\n'
                         '3. 성적표\n'
                         '4. 자동 성적표\n'
                         '5. 주사위\n'
                         '6. 원하는 범위 내 난수 생성\n'
                         '7. 랜덤 이름 추출\n'
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
            q2 = Quiz02Bmi(input('이름 : '), float(input('키 : ')), float(input('몸무게 : ')))
            s += f'{q2.name}님의 비만도 결과는 {q2.getBmi()}입니다.'
        elif menu == 3:
            for i in ['김유신', '강감찬', '유관순']:
                print(i)
            q3 = Quiz03Grade(input('이름 : '), int(input('국어 점수 : ')), int(input('영어 점수 : ')), int(input('수학 점수 : ')))
            s += f'[성적표]\n이름 : {q3.name}\n국어 점수 : {q3.kor}\n영어 점수 : {q3.eng}\n수학 점수 : {q3.math}\n평균 : {q3.avg:.2f}\n합격 여부 : {q3.checkPass()}\n학점 : {q3.getGrade()}'
        elif menu == 4:
            pass
        elif menu == 5:
            s += f'주사위 숫자 : {Quiz05Dice.cast()}'
        elif menu == 6:
            q6 = Quiz06RandomGenerator(int(input('시작값 : ')), int(input('끝값 : ')))
            s += f'생성된 난수 : {q6.execute()}'
        elif menu == 7:
            s += f'추출 결과 : {Quiz07RandomChoice().execute()}'
        elif menu == 8:
            q8 = Quiz08Rps(int(input('1~3 사이의 수 입력 : (1 : 가위, 2 : 바위, 3 : 보) ')))
            s += f'{q8.execute()}'
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
            pass
        else:
            s += '0~3 사이의 수를 입력해주세요.'
        print(s)


class Quiz01Calculator:
    def __init__(self, num1, opcode, num2):
        self.num1 = num1
        self.opcode = opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def calculate(self):
        if self.opcode == '+':
            return f'{self.num1} {self.opcode} {self.num2} = {self.add()}'
        elif self.opcode == '-':
            return f'{self.num1} {self.opcode} {self.num2} = {self.sub()}'
        elif self.opcode == '*':
            return f'{self.num1} {self.opcode} {self.num2} = {self.mul()}'
        elif self.opcode == '/':
            return f'{self.num1} {self.opcode} {self.num2} = {self.div()}'
        else:
            return '올바른 연산자를 입력해주세요.'


class Quiz02Bmi:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getBmi(self):
        bmi = self.weight / (self.height * self.height) * 10000
        if bmi >= 35:
            return '고도 비만'
        elif bmi >= 30:
            return '중(重)도 비만 (2단계 비만)'
        elif bmi >= 25:
            return '경도 비만 (1단계 비만)'
        elif bmi >= 23:
            return '과체중'
        elif bmi >= 18.5:
            return '정상'
        else:
            return '저체중'


class Quiz03Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.avg = (self.kor + self.eng + self.math) / 3.0

    def checkPass(self):
        return '합격' if self.avg >= 60 else '불합격'

    def getGrade(self):
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        elif self.avg >= 60:
            return 'D'
        else:
            return 'F'


class Quiz04GradeAuto:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def checkPass(self):
        return '합격' if ((self.kor + self.eng + self.math) / 3.0) >= 60 else '불합격'

    def getGrade(self):
        pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice:
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz06RandomGenerator:
    def __init__(self, start, end): # 원하는 범위의 정수에서 랜덤값 1개 추출
        self.start = start
        self.end = end

    def execute(self):
        return myRandom(self.start, self.end)


class Quiz07RandomChoice:
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '홍정명', '노홍주', '전종현', '정경준', '양정오']

    def execute(self):
        return self.members[myRandom(0, 23)]


class Quiz08Rps:
    def __init__(self, user):
        self.user = user
        self.com = myRandom(1, 3)

    def execute(self):
        u = self.user
        c = self.com
        arr = ['가위', '바위', '보', 'Draw', 'Win', 'Lose']
        i = 3
        if abs(u - c) == 1:
            i = 4 if u > self.com else 5
        elif abs(u - c) == 2:
            i = 5 if u > c else 4
        return f'user : {arr[u - 1]}, com : {arr[c - 1]} \n결과 : {arr[i]}'


class Quiz09GetPrime:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def execute(self):
        s = ''
        for i in range(self.start, self.end + 1):
            flag = 1
            if i == 1:
                flag = 0
                continue
            for j in range(2, i):
                if i % j == 0:
                    flag = 0
                    break
            if flag == 1:
                s += str(i) + ' '
        return s


class Quiz10LeapYear:
    def __init__(self, year):
        self.year = year

    def execute(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return f'{self.year}년은 윤년입니다.'
        else:
            return f'{self.year}년은 평년입니다.'


class Quiz11NumberGolf:
    def __init__(self):
        self.answer = myRandom(1, 100)

    def execute(self):
        count = 0
        while 1:
            count += 1
            num = int(input('1~100 사이의 숫자 입력 : '))
            if num == self.answer:
                return f'정답입니다. {count}번 만에 맞히셨습니다.'
            elif num > self.answer:
                print('더 작은 수를 입력하세요.')
            elif num < self.answer:
                print('더 큰 수를 입력하세요.')
            else:
                print('잘못 입력하셨습니다.')


class Quiz12Lotto:
    def __init__(self):
        self.answer = []
        num = 0
        duplicate = 1
        for i in range(6):
            duplicate = 1
            while duplicate:
                num = myRandom(1, 45)
                duplicate = 0
                for j in range(i):
                    if self.answer[j] == num:
                        duplicate = 1
                        break
            self.answer.append(num)

        self.numbers = []
        for i in range(6):
            self.numbers.append(int(input('1~45까지의 숫자 6개를 입력해주세요 (중복 불가) : ')))

    def execute(self):
        count = 0
        for i in range(6):
            for j in range(6):
                if self.numbers[j] == self.answer[i]:
                    count += 1
        s = '이번주 로또 번호 : '
        for i in range(6):
            s += str(self.answer[i]) + ' '
        if count == 6:
            s += '\n1등입니다.'
        elif count == 5:
            s += '\n2등입니다.'
        elif count == 4:
            s += '\n3등입니다.'
        else:
            s += '\n낙첨되었습니다.'
        return s


if __name__ == '__main__':
    main()
