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

    def checkPass(self):
        return '합격' if ((self.kor + self.eng + self.math) / 3.0) >= 60 else '불합격'

    def getGrade(self):
        pass


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


class Dice:
    pass


if __name__ == '__main__':
    while 1:
        menu = int(input('\n0. Exit\n1. 계산기\n2. BMI\n3. 성적표\n'))
        s = '*' * 30 + '\n'
        if menu == 0:
            break
        elif menu == 1:
            calc = Quiz01Calculator(int(input('첫 번째 숫자 : ')), input('연산자 (+, -, *, /) : '), int(input('두 번째 숫자 : ')))
            s += calc.calculate()
        elif menu == 2:
            member = Quiz02Bmi(input('이름 : '), float(input('키 : ')), float(input('몸무게 : ')))
            s += f'{member.name}님의 비만도 결과는 {member.getBmi()}입니다.'
        elif menu == 3:
            for i in ['김유신', '강감찬', '유관순']:
                print(i)

            member = Quiz03Grade(input('이름 : '), int(input('국어 점수 : ')), int(input('영어 점수 : ')), int(input('수학 점수 : ')))
            s += f'[성적표]\n이름 : {member.name}\n국어 점수 : {member.kor}\n영어 점수 : {member.eng}\n수학 점수 : {member.math}\n합격 여부 : {member.checkPass()}'
        else:
            s += '0~3 사이의 수를 입력해주세요.'
        print(s)
