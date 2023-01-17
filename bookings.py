import pandas as pd
bookings = pd.read_csv('bookings.csv', encoding='windows-1251', sep=';')
#Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания
bookings.columns = bookings.columns.str.replace(' ', '_')
bookings.columns = bookings.columns.str.lower()
#Пользователи из каких стран совершили наибольшее число успешных бронирований, укажите топ-5
