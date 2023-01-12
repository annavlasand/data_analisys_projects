import pandas as pd
taxi = pd.read_csv('2_taxi_nyc.csv', encoding='windows-1251', sep=',')
taxi.columns = taxi.columns.str.replace(' ', '_')
#общее количество поездок без группировки
all_pickups = taxi['pickups'].sum()
#название района с наименьшим числом поездок
min_pickups = taxi.groupby('borough').agg({'pickups': 'sum'}).idxmin()
print(min_pickups)
