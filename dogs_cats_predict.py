import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree

dogs_n_cats_train = pd.read_csv("dogs_n_cats.csv", sep=',')
dogs_n_cats_test = pd.read_json('dataset_209691_15.txt', encoding='windows-1251')

X = dogs_n_cats_train.drop(['Вид'], axis=1)
y = dogs_n_cats_train.Вид
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)
clf.fit(X_train, y_train)
dogs_n_cats_train[:2]
dogs_n_cats_test[:2]
clf.predict(dogs_n_cats_test).tolist().count('собачка') #предсказанное количество собачек в тестовом датасете