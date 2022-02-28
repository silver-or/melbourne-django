class Calculator(object):
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


if __name__ == '__main__':
    while 1:
        menu = int(input('0. Exit \n1. 계산기 \n'))
        s = '*' * 30 + '\n'
        if menu == 0:
            break
        elif menu == 1:
            num1 = int(input('첫 번째 숫자 : '))
            opcode = input('연산자 (+, -, *, /) : ')
            num2 = int(input('두 번째 숫자 : '))
            calc = Calculator(num1, opcode, num2)
            if opcode == '+':
                s += f'{calc.num1} {calc.opcode} {calc.num2} = {calc.add()}'
            elif opcode == '-':
                s += f'{calc.num1} {calc.opcode} {calc.num2} = {calc.sub()}'
            elif opcode == '*':
                s += f'{calc.num1} {calc.opcode} {calc.num2} = {calc.mul()}'
            elif opcode == '/':
                s += f'{calc.num1} {calc.opcode} {calc.num2} = {calc.div()}'
            else:
                s += '올바른 연산자를 입력해주세요.'
        else:
            s += '0~5 사이의 수를 입력해주세요.'
        print(s)
