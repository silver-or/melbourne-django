import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

from hello import Quiz00
from hello.domains import myRandom


class Quiz20:

    @staticmethod
    def quiz20list() -> None:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])
        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])
        list3 = [1, '2', [1, 2, 3]]
        print(list3)
        # 리스트 연산
        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)
        list4.append(list5)
        print(list4)
        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)
        # 리스트 관련 함수
        a = range(10)
        print(a)
        print(sum(a))
        b = [2, 10, 0, -2]
        print(sorted(b))
        print(b.index(0), len(b))
        return None

    @staticmethod
    def quiz21tuple() -> None:
        a = (1, 2)
        print(a, type(a))
        # a[0] = 4 # error
        a = (1, 2)
        b = (0, (1, 4))
        print(a + b)
        return None

    @staticmethod
    def quiz22dict() -> None:
        a = {"class": ['deep learning', 'machine learning'], "num_students": [40, 20]}
        print(type(a))
        print(a["class"])
        a['grade'] = ['A', 'B', 'C']
        print(a)
        print(a.keys())
        print(list(a.keys()))
        print(a.values())
        print(a.items())
        print(a.get('class'))
        print("class" in a)
        return None

    @staticmethod
    def quiz23listcom() -> None:
        print('---------- legacy ----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('---------- comprehension ----------')
        a2 = [i for i in range(5)]
        print(a2)
        print('---------- comprehension + join ----------')
        print(''.join(str(i) for i in range(5)))
        return None

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs. lxml
        """
        print(soup.prettify())
        artists = soup.find_all('p', {'class': 'artist'})
        print(type(artists))  # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]  # type(artists) : <class 'list'>
        print(''.join(i for i in artists))
        """
        # self.print_music_list(soup) # 아티스트와 타이틀을 분리해서 출력하기
        # self.find_rank(soup) # 랭킹 보기
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        # self.dict1(ls1, ls2)  # 방법 1. 수열 (range) 로 처리
        # self.dict2(ls1, ls2)  # 방법 2. enumerate 로 처리
        # self.dict3(ls1, ls2)  # 방법 3. zip 으로 처리 (권장)
        l1 = [i + j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))  # 최종본
        d1 = {i: j for i, j in zip(ls1, ls2)}
        d2 = dict(zip(ls1, ls2))  # 최종본
        return d2

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    @staticmethod
    def print_music_list(soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))

        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup) -> None:
        for i in ['artist', 'title']:
            res = f'***** {i} ******\n'
            res += ''.join(f'<{j+1}위> {k}\n' for j, k in enumerate(self.find_music(soup, i)))
            print(res)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]

    @staticmethod
    def quiz25dictcom() -> None:
        q = Quiz00()
        students = set([q.quiz06member_choice() for i in range(5)])
        while len(students) != 5:
            students.add(q.quiz06member_choice())
        students = list(students)
        scores = [myRandom(0, 100) for i in range(5)]
        dt = dict(zip(students, scores))
        print(dt)
        return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        titles = soup.find_all('div', {'class': 'ellipsis rank01'})
        print(''.join(i.get_text() for i in titles))
        return None

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')
        return None

    def quiz29(self) -> str:
        a = [i if i == 0 or i == 0 else i for i in range(1)]
        b = [i if i == 0 and i == 0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = ''.join(i for i in [])
        return None
