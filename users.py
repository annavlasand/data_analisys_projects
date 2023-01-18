import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

user_data = pd.read_csv('user_data.csv', encoding='windows-1251', sep=',')
logs = pd.read_csv('logs.csv', encoding='windows-1251', sep=',')

#Какой клиент совершил больше всего успешных операций?
logs_success = logs.query('success == True') \
    .groupby('client', as_index = False) \
    .agg({'success': 'count'}) \
    .rename(columns={'success': 'operations'}) \
    .sort_values(by=['operations'], ascending=False)   #отбираем успешных пользователей
maximum_success = logs_success.operations.max() #максимальное значение количества операций
successful_clients = logs_success.query('operations == @maximum_success') \
    .sort_values('client') \
    .client \
    .to_list() #формируем список из id клиентов, которые совершили максимальное количество успешных операций

#С какой платформы было совершено наибольшее количество успешных операций?
platform_success = logs.query('success == True') \
    .groupby('platform', as_index = False) \
    .agg({'success': 'count'}) \
    .rename(columns={'success': 'operations'}) \
    .sort_values(by=['operations'], ascending=False)

#Какая платформа наиболее популярна среди премиумных клиентов?
#объединяем таблицы logs и user_data
platform_premium = logs.merge(user_data) \
    .query('premium == True') \
    .groupby('platform', as_index = False) \
    .agg({'success': 'count'}) \
    .rename(columns={'success': 'operations'}) \
    .sort_values(by=['operations'], ascending=False)

#распределение возраста клиентов в зависимости от типа клиента (премиум или нет)
data = user_data.merge(logs)

ax = sns.distplot(data.query('premium == True').age)
ax = sns.distplot(data.query('premium == False').age)
plt.show()