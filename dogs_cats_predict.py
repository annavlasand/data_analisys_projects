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

iris_data_train = pd.read_csv('dogs_n_cats.csv', encoding='windows-1251', sep=',')
