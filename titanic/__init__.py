# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.views import View

if __name__ == '__main__':
    def print_menu():
        print('1. 전처리')
        return input('메뉴 선택 : ')

    view = View()
    while 1:
        menu = print_menu()
        if menu == '1':
            print(' #### 전처리 #### ')
            view.preprocess('train.csv', 'test.csv')
            break
        else:
            break
