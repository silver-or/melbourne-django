from context.models import Model
from context.domains import Dataset
from titanic import TitanicModel


class TitanicTemplate:
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.titanic = TitanicModel(train_fname=train_fname, test_fname=test_fname)
