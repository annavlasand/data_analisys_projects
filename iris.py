import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
from IPython.display import SVG
from graphviz import Source
from IPython.display import display
from IPython.display import HTML
style = '<style>svg{width:70% !important;height:70% !important;}</style>'
HTML(style)

iris_data_train = pd.read_csv('C:\\Users\\anvla\\PycharmProjects\\miniprojects_data_analisys\\train_iris.csv', encoding='windows-1251', sep=',')
iris_data_test = pd.read_csv('C:\\Users\\anvla\\PycharmProjects\\miniprojects_data_analisys\\test_iris.csv', encoding='windows-1251', sep=',')

X_train = iris_data_train.drop(['Unnamed: 0', 'species'], axis=1)
X_test = iris_data_test.drop(['Unnamed: 0', 'species'], axis=1)
y_train = iris_data_train.species
y_test = iris_data_test.species

rs = np.random.seed(0)
score_data = pd.DataFrame()
max_depth_values = range(1, 100)

for max_depth in max_depth_values:
    clf = tree.DecisionTreeClassifier(criterion='entropy',
                                      max_depth=max_depth,
                                      random_state=rs)
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)

    mean_cross_val_score = cross_val_score(clf, X_train, y_train, cv=5).mean()

    temp_score_data = pd.DataFrame({'max_depth': [max_depth],
                                    'train_score': [train_score],
                                    'test_score': [test_score],
                                    'cross_val_score': [mean_cross_val_score]})

    scores_data = pd.concat([scores_data, temp_score_data])

scores_data_long = pd.melt(scores_data, id_vars=['max_depth'],
                           value_vars=['train_score', 'test_score', 'cross_val_score'],
                           var_name='set_type',
                           value_name='score')
sns.lineplot(x='max_depth', y='score', hue='set_type', data=scores_data_long)