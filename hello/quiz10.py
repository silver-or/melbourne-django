import random

from hello.domains import my100, myRandom


class Quiz10:

    def quiz10bubble(self) -> str: return None

    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str:
        start = my100()
        end = myRandom(start, start * 2)
        s = ''
        for i in range(start, end + 1):
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
        print(f'{start} ~ {end} 까지의 소수 : {s}')
        return None

    def quiz18golf(self) -> str:
        answer = my100()
        count = 0
        s = ''
        while 1:
            count += 1
            num = int(input('1~100 사이의 숫자 입력 : '))
            if num == answer:
                s = f'정답입니다. {count}번 만에 맞히셨습니다.'
            elif num > answer:
                s = f'더 작은 수를 입력하세요.'
            elif num < answer:
                s = f'더 큰 수를 입력하세요.'
            else:
                s = '1~100 사이의 숫자를 입력해주세요.'
            print(s)
        return None

    def quiz19booking(self) -> str: return None