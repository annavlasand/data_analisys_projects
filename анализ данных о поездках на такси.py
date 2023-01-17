import pandas as pd
taxi = pd.read_csv('2_taxi_nyc.csv', encoding='windows-1251', sep=',')
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


print(temp_to_celcius(taxi['temp'][:5]))
