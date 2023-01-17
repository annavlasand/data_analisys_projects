import pandas as pd
bookings = pd.read_csv('bookings.csv', encoding='windows-1251', sep=';')
#Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания
bookings.columns = bookings.columns.str.replace(' ', '_')
bookings.columns = bookings.columns.str.lower()
#Пользователи из каких стран совершили наибольшее число успешных бронирований, укажите топ-5
is_canceled = bookings.query('is_canceled == 0').country.value_counts()[:5]
#На сколько ночей в среднем бронируют отели разных типов?
nights = bookings.groupby('hotel').agg({'stays_total_nights': 'mean'}).round(2)

