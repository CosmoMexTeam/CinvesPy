# coding: utf-8
# This Pipeline is a simple example
import sys
import luigi
import pandas as pd
import pdb

from luigi import configuration
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline

class IrisData(luigi.ExternalTask):
    def output(self):
        return luigi.LocalTarget("../data/iris.csv")

class TrainTestSplit(luigi.Task):
    features = luigi.Parameter()

    def requires(self):
        return IrisData()

    def output(self):
        return {
            'X_train': luigi.LocalTarget("../data/X_train.csv"),
            'X_test': luigi.LocalTarget("../data/X_test.csv"),
            'y_train': luigi.LocalTarget("../data/y_train.csv"),
            'y_test': luigi.LocalTarget("../data/y_test.csv")
        }

    def run(self):
        cols = [
            "Sepal_Length",
            "Sepal_Width",
            "Petal_Length",
            "Petal_Width",
            "Species"
        ]
        features = [x.strip() for x in self.features.split(",")]

        iris_df = pd.read_csv(self.input().path, names=cols)

        X = iris_df[features]
        y = iris_df["Species"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

        X_train.to_csv(self.output()['X_train'].path, index = False, header = True)
        X_test.to_csv(self.output()['X_test'].path, index = False, header = True)
        y_train.to_csv(self.output()['y_train'].path, index = False, header = True)
        y_test.to_csv(self.output()['y_test'].path, index = False, header = True)

class TrainModel(luigi.Task):
    features = luigi.Parameter()
    algorithm = luigi.Parameter()
    parameters = luigi.DictParameter()

    def requires(self):
        return TrainTestSplit()

    def output(self):
        return {
            'model': luigi.LocalTarget("../outputs/" + self.algorithm + "_model.pkl"),
            'metadata': luigi.LocalTarget("../outputs/" + self.algorithm + "_metadata.txt")
        }

    def run(self):
        parameters = dict(self.parameters)
        X_train = pd.read_csv(self.input()['X_train'].path)
        y_train = pd.read_csv(self.input()['y_train'].path)

        if self.algorithm == 'RF':
            model = RandomForestClassifier(
                    n_estimators=int(parameters['n_estimators']),
                    max_features='sqrt',
                    criterion=parameters['criterion'],
                    max_depth=int(parameters['max_depth']),
                    min_samples_split=int(parameters['min_samples_split']),
                    random_state=int(parameters['random_state']))

        elif self.algorithm == 'LR':
            lr = LogisticRegression(
                    C=int(parameters['c_reg']),
                    random_state=int(parameters['random_state']),
                    penalty=parameters['penalty'])
            model = make_pipeline(StandardScaler(), lr)

        # Train model
        model.fit(X_train, y_train)
        # Store model
        joblib.dump(model, self.output()['model'].path)
        with self.output()['metadata'].open('w') as meta:
            meta.write(str(model))

class IrisPipeline(luigi.WrapperTask):
    models = luigi.Parameter('DEFAULT')
    features = luigi.Parameter('DEFAULT')

    def requires(self):
        tasks = []
        models = [x.strip() for x in self.models.split(',')]
        for model in models:
            params = configuration.get_config()[model]
            tasks.append(TrainModel(features=self.features,
                                    algorithm=model,
                                    parameters=dict(params)))
        return tasks

