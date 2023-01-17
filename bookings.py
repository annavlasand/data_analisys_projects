import pandas as pd
bookings = pd.read_csv('bookings.csv', encoding='windows-1251', sep=';')

#Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания
bookings.columns = bookings.columns.str.replace(' ', '_')
bookings.columns = bookings.columns.str.lower()

#Пользователи из каких стран совершили наибольшее число успешных бронирований, укажите топ-5
is_canceled = bookings.query('is_canceled == 0').country.value_counts()[:5]

#На сколько ночей в среднем бронируют отели разных типов?
nights = bookings.groupby('hotel').agg({'stays_total_nights': 'mean'}).round(2)

'''Иногда тип номера, полученного клиентом (assigned_room_type), отличается 
от изначально забронированного (reserved_room_type). 
Такое может произойти, например, по причине овербукинга. 
Сколько подобных наблюдений встретилось в датасете?
*отмена бронирования также считается'''
dif_room_types = bookings.query('assigned_room_type != reserved_room_type').shape

'''Проанализируйте даты запланированного прибытия. 
– На какой месяц чаще всего успешно оформляли бронь в 2016? 
Изменился ли самый популярный месяц в 2017?'''
arrival_2016 = bookings.query('arrival_date_year == 2016').arrival_date_month.value_counts()
arrival_2017 = bookings.query('arrival_date_year == 2017').arrival_date_month.value_counts()

'''Сгруппируйте данные по годам, а затем проверьте, на какой месяц 
бронирования отеля типа City Hotel отменялись чаще всего в 2015? 2016? 2017?'''
year_2015_2016_2017 = bookings.loc[bookings.query("is_canceled == 1 & hotel == 'City Hotel'").index]\
    .groupby('arrival_date_year').arrival_date_month.value_counts()

''''Посмотрите на числовые характеристики трёх колонок: adults, children и babies. 
Какая из них имеет наибольшее среднее значение?'''
mean_num = bookings[['adults', 'children', 'babies']].mean()








