import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

taxi = pd.read_csv('2_taxi_nyc.csv', encoding='windows-1251', sep=',')
taxi_peru = pd.read_csv('taxi_peru.csv', encoding='windows-1251', sep=';', parse_dates=['start_at', 'end_at', 'arrived_at'])


#замена все пробелы в названии колонок на нижние подчеркивания:
taxi.columns = taxi.columns.str.replace(' ', '_')

#общее количество поездок без группировки:
all_pickups = taxi['pickups'].sum()

#название района с наименьшим числом поездок:
min_pickups = taxi.groupby('borough').agg({'pickups': 'sum'}).idxmin()

#группировка по району и праздничным дням:
hd_pickups = taxi.groupby(['borough', 'hday']).agg({'pickups': 'mean'})

#число поездок по месяцам для каждого района
pickups_by_mon_bor = taxi.groupby(['borough', 'pickup_month'], as_index = False).agg({'pickups': 'sum'}).sort_values(by='pickups', ascending=False)

#функция перевода градусов Фаренгейта в Цельсия
def temp_to_celcius(temp):
    return (temp - 32) * 5 / 9

#с какой платформы было сделано больше всего заказов (data_set = taxi_peru)
max_source = taxi_peru.source.value_counts(normalize=True).max

#визуализируем данные, с какой платформы было сделано больше всего заказов
taxi_counts = (taxi_peru['source'].value_counts()
               .reset_index()
               .rename({'index':'source', 'source':'cnt'}, axis='columns'))
ax = sns.barplot(x='source', y='cnt', data=taxi_counts)
ax.set(xlabel='Platform', ylabel='Count')
sns.despine()
plt.show()

#какой тип поездки (icon) встречался чаще всего
a = sns.countplot(x='icon', data=taxi_peru)
a.set(xlabel='Icon', ylabel='Count')
sns.despine()
plt.show()

#визуализируем распределение переменной end_state (итоговое состояние заказа) в разбивке по платформам (source)
plt.figure(figsize=(4,3))
sns.countplot(data=taxi_peru, hue='end_state', x='source')
plt.show()

#как распределены оценки водителей
driver_score_counts = taxi_peru.driver_score.value_counts(normalize=True) \
    .mul(100).round(2) \
    .reset_index() \
    .rename({'index':'driver_score', 'driver_score':'percentage'}, axis='columns') \
    .sort_values(by=['driver_score'])

#визуализируем распределение оценок водителей
ax = sns.barplot(x='driver_score', y='percentage', data=driver_score_counts, color='blue', alpha=0.5)
ax.set(xlabel='Driver score', ylabel='Percentage')
sns.despine()
plt.show()