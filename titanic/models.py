from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel:
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.dataset.train = self.model.new_model(train_fname)
        self.dataset.test = self.model.new_model(test_fname)
        # id 추출
        ic(self.dataset.train.columns)  # 트레인 컬럼
        ic(self.dataset.train.head())  # 트레인 헤드 : 첫 다섯 개의 데이터
        ic(self.dataset.train)

    def preprocess(self):
        df = self.dataset.train
        garbage_ls = [self.sibsp_garbage, self.parch_garbage, self.ticket_garbage, self.cabin_garbage]
        for garbage in garbage_ls:
            df = garbage(df)
        # df = self.sibsp_garbage(df)
        # df = self.parch_garbage(df)
        # df = self.ticket_garbage(df)
        # df = self.cabin_garbage(df)
        df = self.name_nominal(df)
        df = self.sex_nominal(df)
        df = self.embarked_nominal(df)
        df = self.pclass_ordinal(df)
        df = self.age_ratio(df)
        df = self.fare_ratio(df)
        df = self.create_label(df)
        df = self.create_train(df)
        # final df는 정제된 상태

    @staticmethod
    def create_label(df) -> object:
        return df

    @staticmethod
    def create_train(df) -> object:
        return df

    @staticmethod
    def drop_feature(df) -> object:
        return df
    '''
    Categorical vs. Quantitative
    Cate → nominal (이름) vs. ordinal (순서)
    Quan → interval (상대) vs. ratio (절대)
    '''
    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_nominal(df) -> object:
        return df

    @staticmethod
    def sex_nominal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    def sibsp_garbage(self, df) -> object:
        return self.drop_feature(df)

    def parch_garbage(self, df) -> object:
        return self.drop_feature(df)

    def ticket_garbage(self, df) -> object:
        return self.drop_feature(df)

    @staticmethod
    def fare_ratio(df) -> object:
        return df

    def cabin_garbage(self, df) -> object:
        return self.drop_feature(df)

    @staticmethod
    def embarked_nominal(df) -> object:
        return df
