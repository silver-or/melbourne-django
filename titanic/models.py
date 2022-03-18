from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel:
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname) -> object:  # 데이터 가공 후 리턴
        this = self.dataset  # this : model = titanic
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        # Entity에서 Object로 전환
        this.train = this.train.drop(feature[1], axis=1)  # 정답 제거 # axis : 축 → row : 0, col : 1
        this = self.drop_feature(this, feature[6], feature[7], feature[8], feature[10])
        self.kwargs_sample(name='이순신')
        '''
        this = self.drop_feature(this)
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.create_train(this)
        '''
        self.print_this(this)
        return this  # final df는 정제된 상태

    @staticmethod
    def print_this(this):
        # this = self.dataset
        print('*' * 100)
        ic(f'1. Train 의 타입 : {type(this.train)} \n')
        ic(f'2. Train 의 컬럼 : {this.train.columns} \n')  # property (앞으로 가공할 예정)
        ic(f'3. Train 의 상위 1개 : {this.train.head(1)} \n')  # method
        ic(f'4. Train 의 null 개수 : {this.train.isnull().sum()} \n')
        ic(f'5. Test 의 타입 : {type(this.test)} \n')
        ic(f'6. Test 의 컬럼 : {this.test.columns} \n')
        ic(f'7. Test 의 상위 1개 : {this.test.head(1)} \n')
        ic(f'8. Test 의 null 개수 : {this.test.isnull().sum()} \n')
        ic(f'9. id 타입 : {type(this.id)} \n')
        ic(f'10. id 상위 10개 : {this.id[:10]} \n')
        print('*' * 100)

    @staticmethod
    def drop_feature(this, *feature) -> object:
        # [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]  # inplace : 원본 훼손 (데이터 유실)의 가능성 존재
        [i.drop(list(feature), axis=1, inplace=True) for i in [this.train, this.test]]
        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))  # ic| type(kwargs): <class 'dict'>
        {print(''.join(f'key : {i}, val : {j}')) for i, j in kwargs.items()}  # key : name, val : 이순신
    '''
    Categorical vs. Quantitative
    Cate → nominal (이름) vs. ordinal (순서)
    Quan → interval (상대) vs. ratio (절대)
    '''
    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this
