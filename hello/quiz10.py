import random

from hello.domains import my100


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
        end = my100()
        while 1:
            start = my100()
            end = my100()
            if end > start:
                break
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

    def quiz18golf(self) -> str: return None

    def quiz19booking(self) -> str: return None