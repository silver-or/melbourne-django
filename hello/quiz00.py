from hello import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        op = ['+', '-', '*', '/', '%']
        opcode = op[myRandom(0, 4)]
        s = f'{a} {opcode} {b} = '
        if opcode == '+':
            s += f'{self.add(a, b)}'
        elif opcode == '-':
            s += f'{self.sub(a, b)}'
        elif opcode == '*':
            s += f'{self.mul(a, b)}'
        elif opcode == '/':
            s += f'{self.div(a, b)}'
        else:
            s += f'{self.mod(a, b)}'
        print(s)
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = members()[myRandom(0, 23)]
        this.height = myRandom(160, 190)
        this.weight = myRandom(50, 100)
        bmi = this.weight / (this.height * this.height) * 10000
        s = f'{this.name}님의 비만도 결과 : '
        if bmi >= 35:
            s += '고도 비만'
        elif bmi >= 30:
            s += '중(重)도 비만 (2단계 비만)'
        elif bmi >= 25:
            s += '경도 비만 (1단계 비만)'
        elif bmi >= 23:
            s += '과체중'
        elif bmi >= 18.5:
            s += '정상'
        else:
            s += '저체중'
        print(s)

    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        u = myRandom(1, 3)
        c = myRandom(1, 3)
        arr = ['가위', '바위', '보', 'Draw', 'Win', 'Lose']
        i = 3
        if abs(u - c) == 1:
            i = 4 if u > c else 5
        elif abs(u - c) == 2:
            i = 5 if u > c else 4
        print(f'user : {arr[u - 1]}, com : {arr[c - 1]} \n결과 : {arr[i]}')

    def quiz04leap(self):
        year = myRandom(1960, 2022)
        print(f'{year}년은 윤년입니다.' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else f'{year}년은 평년입니다.')

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        hap = self.hap(kor, eng, math)
        avg = self.avg(hap)
        grade = self.getGrade(avg)
        passChk = self.passChk(avg)
        print(f'국어 점수 : {kor}\n영어 점수 : {eng}\n수학 점수 : {math}\n합계 : {hap}\n평균 : {avg:.2f}\n학점 : {grade}\n합격 여부 : {passChk}')

    def hap(self, kor, eng, math):
        return kor + eng + math

    def avg(self, hap):
        return hap / 3.0

    def getGrade(self, avg):
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def passChk(self, avg):  # 60점 이상 이면 합격
        return '합격' if avg >= 60 else '불합격'

    def quiz06memberChoice(self):
        print(members()[myRandom(0, 23)])

    def quiz07lotto(self):
        answer = []
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
            if num not in answer:
                answer.append(num)
            else:
                i += 1

        numbers = []
        for i in range(6):
            numbers.append(int(input('1~45까지의 숫자 6개를 입력해주세요 (중복 불가) : ')))

        count = 0
        for i in range(6):
            if numbers[i] in answer:
                count += 1

        s = '이번주 로또 번호 : '
        for i in answer:
            s += str(i) + ' '
        if count == 6:
            s += '\n1등입니다.'
        elif count == 5:
            s += '\n2등입니다.'
        elif count == 4:
            s += '\n3등입니다.'
        else:
            s += '\n낙첨되었습니다.'
        print(s)

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        name = members()[myRandom(0, 23)]
        bal = 0
        while 1:
            menu = int(input('0. Exit\n1. 입금\n2. 출금\n'))
            if menu == 0:
                break
            elif menu == 1:
                money = myRandom(100, 10000)
                bal = self.deposit(bal, money)
            elif menu == 2:
                money = myRandom(100, 10000)
                bal = self.withdraw(bal, money)
            print(f'{name}님의 잔고 : {bal}') if bal is not None else print(f'{name}님의 잔고 : 0')

    def deposit(self, bal, money):
        if bal is not None:
            bal += money
        else:
            bal = money
        return bal

    def withdraw(self, bal, money):
        if bal is not None and bal >= money:
            bal -= money
            return bal
        else:
            print('잔고가 부족합니다.')

    def quiz09gugudan(self):  # 책받침구구단
        s = ''
        for k in range(2, 7, 4):
            for i in range(1, 10):
                for j in range(k, k + 4):
                    s += f'{j} * {i} = {i * j} \t'
                s += '\n'
            s += '\n'
        print(s)
