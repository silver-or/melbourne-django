import random


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
    @staticmethod
    def getBmi(member):
        this = member
        bmi = this.weight / (this.height * this.height) * 10000
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
        self.members = ['최민서', '한성수', '김윤섭', '김승현',
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '강민', '최건일', '유재혁', '김아름', '장원종']

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
            i = 4 if u > c else 5
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
        year = self.year
        return f'{year}년은 윤년입니다.' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else f'{year}년은 평년입니다.'


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
                print('1~100 사이의 숫자를 입력해주세요.')


class Quiz12Lotto:
    def __init__(self):
        self.answer = []
        num = 0
        duplicate = 1
        '''
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
        '''
        for i in range(6):
            num = myRandom(1, 45)
            if num not in self.answer:
                self.answer.append(num)
                print(num)

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


class Quiz13Bank:
    def __init__(self):
        self.bal = 0

    def execute(self):
        while 1:
            menu = int(input('0. Exit\n1. 입금\n2. 출금\n'))
            if menu == 0:
                break
            elif menu == 1:
                self.deposit(int(input('금액 입력 : ')))
            elif menu == 2:
                self.withdraw(int(input('금액 입력 : ')))
            print(f'잔고 : {self.bal}')
        return f'최종 잔고 : {self.bal}'

    def deposit(self, money):
        self.bal += money

    def withdraw(self, money):
        if self.bal >= money:
            self.bal -= money
        else:
            print('잔고가 부족합니다.')


class Quiz14Gugudan:
    @staticmethod
    def execute():
        s = ''
        for k in range(2, 7, 4):
            for i in range(1, 10):
                for j in range(k, k+4):
                    s += f'{j} * {i} = {i * j} \t'
                s += '\n'
            s += '\n'
        return s


if __name__ == '__main__':
    main()
